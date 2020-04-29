import os
import pandas as pd
import numpy as np
import functools
import logging
from sklearn.datasets import fetch_20newsgroups

import feature_extraction
import feature_projection

logger = logging.getLogger(__name__)

DATA_PATH = '/Users/gbpcosta/datasets'


def load_20newsgroups():
    df = pd.DataFrame()

    dataset = fetch_20newsgroups(subset='all')

    df['data'] = dataset.data
    df['label'] = dataset.target
    df['id'] = pd.Series(np.arange(df.shape[0]))

    return df


def load_real_or_fake_jobs_dataset():
    df = pd.read_csv(
        os.path.join(DATA_PATH,
                     'real-or-fake-jobposting/fake_job_postings.csv'))

    df['data'] = df.apply(lambda x: ', '.join(x[['title',
                                                 'department',
                                                 'location',
                                                 'salary_range',
                                                 'description',
                                                 'requirements',
                                                 'benefits',
                                                 'company_profile',
                                                 'industry',
                                                 'function',
                                                 'employment_type',
                                                 'required_experience',
                                                 'required_education']].dropna()), axis=1)
    df['label'] = df['fraudulent']
    df['id'] = df['job_id'].copy()

    return df


def load_dataset(dataset_name):
    if dataset_name == 'nlp_jobposts':
        logger.info('Loading Fake/Real Job Post dataset')
        df = load_real_or_fake_jobs_dataset()
    if dataset_name == 'nlp_20newsgroups':
        logger.info('Loading 20 Newsgroups dataset')
        df = load_20newsgroups()
    else:
        logger.error(f'Unknown dataset selected: {dataset_name}')
        raise RuntimeError

    logger.info('Dataset loaded!')

    return df


def extract_features(df, feat_name):
    logger.info(f'Extracting features using {feat_name}')
    if feat_name == 'nlp_glove':
        feats = feature_extraction.get_batch_glove_vector_doc(df['data'].values)
    elif feat_name == 'nlp_bert':
        feats = feature_extraction.get_batch_bert_vector_doc(df['data'].values)
    else:
        raise RuntimeError

    feats = pd.DataFrame(np.stack(feats), index=df.index)

    logger.info('Features extracted!')

    return feats


def project_features(feats, feat_proj_name):
    logger.info(f'Projecting features to a 2D space using {feat_proj_name}')
    if feat_proj_name == 'proj_pca':
        proj_feats, proj_model = feature_projection.get_pca_projection(feats)
    elif feat_proj_name == 'proj_lda':
        proj_feats, proj_model = feature_projection.get_lda_projection(feats)
    elif feat_proj_name == 'proj_tsne':
        proj_feats, proj_model = feature_projection.get_tsne_projection(feats)

    logger.info('2D Features created!')

    return proj_feats, proj_model


def get_data(dataset_name, feat_name, feat_proj_name=None):
    logger.info(f'Loading dataset: {dataset_name}, {feat_name}, {feat_proj_name}')

    filepath = os.path.join(DATA_PATH, f'{dataset_name}.h5')

    key = f'{feat_name}'
    if feat_proj_name:
        key += f'_{feat_proj_name}'

    if not os.path.exists(filepath):
        logger.info(f'File {filepath} does not exists. Creating now! (This will take a while, possibly a long while)')
        generate_preproc_data_file(dataset_name)

    df = pd.read_hdf(filepath, 'original')
    proj_feats = pd.read_hdf(filepath, key)

    logger.info('Dataset ready!')

    return df,  proj_feats


def generate_preproc_data_file(dataset_name, feat_names=['nlp_glove', 'nlp_bert'], feat_proj_names=['proj_pca', 'proj_tsne']):
    logger.info(f'Creating preprocessed data file: {dataset_name} {feat_names} {feat_proj_names}')

    filepath = os.path.join(DATA_PATH, f'{dataset_name}.h5')

    df = load_dataset(dataset_name)

    for feat_name in feat_names:
        feats = extract_features(df, feat_name)

        for feat_proj_name in feat_proj_names:
            proj_feats, proj_model = project_features(feats, feat_proj_name)

            pd.DataFrame(proj_feats,
                         index=df.index,
                         columns=[f'{feat_proj_name.upper()} 1',
                                  f'{feat_proj_name.upper()} 2']).to_hdf(filepath,
                                                                         f'{feat_name}_{feat_proj_name}')

        feats.set_index(df.index).to_hdf(filepath, f'{feat_name}')

    df.to_hdf(filepath, 'original')
