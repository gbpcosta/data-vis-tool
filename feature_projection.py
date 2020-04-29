from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE


def get_pca_projection(feats, n_components=2, whiten=False, random_state=42):
    pca = PCA(n_components=n_components, whiten=whiten,
              random_state=random_state)
    proj_data = pca.fit_transform(feats)

    return proj_data, pca


def get_lda_projection(feats, labels, n_components=2):
    assert (n_components is None) \
        or (n_components <= min(labels.unique().shape[0] - 1, feats.shape[1]))

    lda = LinearDiscriminantAnalysis(n_components=n_components)
    proj_data = lda.fit_transform(feats)

    return proj_data, lda


def get_tsne_projection(feats, n_components=2, perplexity=30.0,
                        early_exaggeration=12.0, learning_rate=200.0,
                        n_iter=1000, n_iter_without_progress=300,
                        min_grad_norm=1e-07, metric='euclidean',
                        init='random', verbose=0, random_state=42,
                        method='barnes_hut', angle=0.5, n_jobs=None):
    tsne = TSNE(n_components=n_components, perplexity=perplexity,
                early_exaggeration=early_exaggeration,
                learning_rate=learning_rate, n_iter=n_iter,
                n_iter_without_progress=n_iter_without_progress,
                min_grad_norm=min_grad_norm, metric=metric, init=init,
                verbose=verbose, random_state=random_state,
                method=method, angle=angle, n_jobs=n_jobs)
    proj_data = tsne.fit_transform(feats)

    return proj_data, tsne
