from app import app
import pandas as pd
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import logging

import data_manipulation
import utils

logger = logging.getLogger(__name__)

# @app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
# def render_page_content(pathname):
#     if pathname in ['/', '/page-1']:
#         return html.P('This is the content of page 1!')
#     elif pathname == '/page-2':
#         return html.P('This is the content of page 2. Yay!')
#     elif pathname == '/page-3':
#         return html.P('Oh cool, this is page 3!')
#     # If the user tries to reach a different page, return a 404 message
#     return dbc.Jumbotron(
#         [
#             html.H1('404: Not found', className='text-danger'),
#             html.Hr(),
#             html.P(f'The pathname {pathname} was not recognised...'),
#         ]
#     )


# @app.callback(
#     [Output('sidebar', 'className'),
#      Output('div-data', 'className')],
#     [Input('sidebar-toggle', 'n_clicks')],
#     [State('sidebar', 'className')],
# )
# def toggle_classname(n, classname):
#     if n and classname == '':
#         return 'collapsed', 'twelve columns div-data'
#     return '', 'nine columns div-data'


# @app.callback(
#     Output('collapse', 'is_open'),
#     [Input('navbar-toggle', 'n_clicks')],
#     [State('collapse', 'is_open')],
# )
# def toggle_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open


@app.callback(
    [Output('div-graph', 'children'),
     Output('div-table', 'children')],
    [Input('dd-dataset', 'value'),
     Input('dd-feat-extraction', 'value'),
     Input('dd-feat-proj', 'value')],
)
def update_graph(dataset_name, feat_name, feat_proj_name):
    if dataset_name in ['nlp_jobposts', 'nlp_20newsgroups']:
        df, proj_feats = data_manipulation.get_data(dataset_name, feat_name, feat_proj_name)
        plt_aux = pd.concat([df, proj_feats], axis=1)
        plt_aux['tooltip_text'] = plt_aux['data'].apply(utils.create_tooltip)
    else:
        raise RuntimeError

    logger.info('Creating new graph (update_data)')

    fig = go.Figure()

    for group, data in plt_aux.groupby('label'):
        fig.add_trace(go.Scatter(
            x=data[data.columns[-2]],
            y=data[data.columns[-3]],
            name=group,
            mode='markers',
            marker=dict(color=utils.COLOR_PALETTE_20[data['label'].values]),
            opacity=0.7,
            text=data['tooltip_text'],
            hovertemplate=utils.TOOLTIP_TEMPLATE
        ))

    fig.update_layout(
        autosize=True,
        height=800,
    )

    logger.info('Created/updated graph!')

    logger.info('Creating new data table (update_data)')

    data_table = dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': col, 'name': col} for col in df.columns],
        tooltip_data=[{
            col: {
                    'type': 'markdown',
                    'value': utils.create_tooltip(df.loc[ii, col])
            } for col in df.columns
        } for ii in range(df.shape[0])],
        style_as_list_view=True,
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        style_table={
            'maxHeight': '500px',
            'overflowY': 'scroll',
            'overflowX': 'scroll',
        },
        style_cell={
            'minWidth': '0px',
            'maxWidth': '180px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
        fixed_rows={
            'headers': True,
            'data': 0
        },
        css=[{'selector': '.row', 'rule': 'margin: 0'}]
    )

    logger.info('Created/updated data table!')
    return [dcc.Graph(id='plot', figure=fig)], data_table
