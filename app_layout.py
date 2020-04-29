import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def define_menu():
    menu = html.Div([
        html.Label('Dataset'),
        # dbc.Col(
        #     dbc.DropdownMenu(
        #         id='dd-dataset',
        #         className='dd-dataset',
        #         label='Dataset',
        #         children=[
        #             dbc.DropdownMenuItem('NLP Datasets', header=True),
        #             dbc.DropdownMenuItem('Fake/Real Job Posts'),
        #             # TODO: Including both NLP and CV datasets will make everything more complicated, so I will leave it for later and focus on NLP for now
        #             # dbc.DropdownMenuItem(divider=True),
        #             # dbc.DropdownMenuItem('CV Datasets', header=True),
        #             # dbc.DropdownMenuItem('MNIST', disabled=True),
        #             # dbc.DropdownMenuItem('CIFAR10', disabled=True),
        #         ],
        #         right=False,
        #         in_navbar=True,
        #     ),
        #     width='auto'
        # ),
        html.Div([
            dcc.Dropdown(
                className='dd-dataset',
                id='dd-dataset',
                options=[
                    {'label': 'NLP Datasets', 'value': '', 'disabled': True},
                    {'label': 'Fake/Real Job Posts', 'value': 'nlp_jobposts'},
                    {'label': '20 Newsgroups', 'value': 'nlp_20newsgroups'},
                    # TODO: Including both NLP and CV datasets will make everything more complicated, so I will leave it for later and focus on NLP for now
                    # {'label': 'CV Datasets', 'value': '', 'disabled': True},
                    # {'label': 'MNIST', 'value': 'cv_mnist'},
                    # {'label': 'Fashion MNIST', 'value': 'cv_fashionmnist'},
                    # {'label': 'CIFAR10', 'value': 'cv_cifar10'}
                ],
                value='nlp_20newsgroups',
                clearable=False
            ),
        ]),

        html.Label('Feature Extraction Method'),
        # dbc.DropdownMenu(
        #     id='dd-feat-extraction',
        #     className='dd-feat-extraction',
        #     label='Feature Extraction',
        #     children=[
        #         # TODO: this needs to be extended to cover NLP and CV descriptors, depending on the dataset selected
        #         dbc.DropdownMenuItem('GloVe'),
        #         dbc.DropdownMenuItem('BERT'),
        #         # TODO: Including both NLP and CV datasets will make everything more complicated, so I will leave it for later and focus on NLP for now
        #         # dbc.DropdownMenuItem(divider=True),
        #         # dbc.DropdownMenuItem('CV Datasets', header=True),
        #         # dbc.DropdownMenuItem('MNIST', disabled=True),
        #         # dbc.DropdownMenuItem('CIFAR10', disabled=True),
        #     ]
        # ),
        html.Div([
            dcc.Dropdown(
                id='dd-feat-extraction',
                options=[
                    # TODO: this needs to be extended to cover NLP and CV descriptors, depending on the dataset selected
                    {'label': 'GloVe', 'value': 'nlp_glove'},
                    {'label': 'BERT', 'value': 'nlp_bert'},
                ],
                value='nlp_glove',
                clearable=False
            ),
        ]),

        html.Label('Feature Projection Method'),
        # dbc.DropdownMenu(
        #     id='dd-feat-proj',
        #     className='dd-feat-proj',
        #     label='Feature Projection',
        #     children=[
        #         # TODO: this needs to be extended to cover NLP and CV descriptors, depending on the dataset selected
        #         dbc.DropdownMenuItem('PCA'),
        #         # TODO: LDA requires another input - label (column where labels are stored)
        #         # dbc.DropdownMenuItem('LDA'),,
        #         dbc.DropdownMenuItem('t-SNE'),
        #     ]
        # ),
        html.Div([
            dcc.Dropdown(
                id='dd-feat-proj',
                options=[
                    # TODO: this needs to be extended to cover NLP and CV descriptors, depending on the dataset selected
                    {'label': 'PCA', 'value': 'proj_pca'},
                    # TODO: LDA requires another input - label (column where labels are stored)
                    # {'label': 'LDA', 'value': 'proj_lda'},
                    {'label': 't-SNE', 'value': 'proj_tsne'},
                ],
                value='proj_pca',
                clearable=False
            ),
        ]),

        html.Label('Datatable Columns'),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value=['MTL', 'SF'],
            multi=True
        ),

        # html.Label('Radio Items'),
        # dcc.RadioItems(
        #     options=[
        #         {'label': 'New York City', 'value': 'NYC'},
        #         {'label': u'Montréal', 'value': 'MTL'},
        #         {'label': 'San Francisco', 'value': 'SF'}
        #     ],
        #     value='MTL'
        # ),

        # html.Label('Checkboxes'),
        # dcc.Checklist(
        #     options=[
        #         {'label': 'New York City', 'value': 'NYC'},
        #         {'label': u'Montréal', 'value': 'MTL'},
        #         {'label': 'San Francisco', 'value': 'SF'}
        #     ],
        #     value=['MTL', 'SF']
        # ),

        html.Hr(),

        html.Label('Text Search'),
        html.Div([
            dbc.Input(id='text-search', placeholder='Search for..', type='search')
        ]),

        # html.Label('Slider'),
        # dcc.Slider(
        #     min=0,
        #     max=9,
        #     marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        #     value=5,
        # ),
    ])

    return menu


def define_sidebar():
    # TODO: make sidebar collapsible and content adjust to space available on screen
    sidebar_header = dbc.Row(
        [
            dbc.Col(html.H2('Menu', className='sidebar-header')),
            # Button to collapse sidebar
            # dbc.Col(
            #     [
            #         # html.Button(
            #         #     # use the Bootstrap navbar-toggler classes to style
            #         #     html.Span(className='navbar-toggler-icon'),
            #         #     className='navbar-toggler',
            #         #     # the navbar-toggler classes don't set color
            #         #     style={
            #         #         'color': 'rgba(0,0,0,.5)',
            #         #         'border-color': 'rgba(0,0,0,.1)',
            #         #     },
            #         #     id='navbar-toggle',
            #         # ),
            #         html.Button(
            #             # use the Bootstrap navbar-toggler classes to style
            #             html.Span(className='navbar-toggler-icon'),
            #             className='navbar-toggler',
            #             # the navbar-toggler classes don't set color
            #             style={
            #                 'color': 'rgba(0,0,0,.5)',
            #                 'border-color': 'rgba(0,0,0,.1)',
            #             },
            #             id='sidebar-toggle',
            #         ),
            #     ],
            #     # the column containing the toggle will be only as wide as the
            #     # toggle, resulting in the toggle being right aligned
            #     width='auto',
            #     # vertically align the toggle in the center
            #     align='center',
            # ),
        ]
    )

    sidebar = html.Div(
        children=[
            sidebar_header,
            # we wrap the horizontal rule and short blurb in a div that can be
            # hidden on a small screen
            html.Div(
                [
                    html.Hr(),
                    html.P(
                        'Use these controls to adjust the visualisation.',
                        className='lead',
                    ),
                ],
                id='blurb',
            ),
            # use the Collapse component to animate hiding / revealing links
            # dbc.Collapse(
            #     children=[
            define_menu(),
            #     ],
            #     id='collapse',
            # ),
        ],
        id='sidebar',
    )

    return sidebar


def define_table(df, max_rows=10):
    return html.Div(
        className='content-table',
        id='content-table',
        children=[
            # dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True,
            #                          responsive=True,)
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=[{'id': col, 'name': col} for col in df.columns],
                tooltip_data=[{
                    col: {
                            'type': 'markdown',
                            'value': create_tooltip(df.loc[ii, col])
                    } for col in df.columns
                } for ii in range(df.shape[0])],
                style_cell_conditional=[
                    {
                        'if': {'column_id': c},
                        'textAlign': 'left'
                    } for c in ['Date', 'Region']
                ],
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
            )
        ],
    )


def define_layout():
    layout = html.Div(
        className='content-div',
        id='content-div',
        children=[
            dcc.Location(id='url'),
            define_sidebar(),
            dbc.Container(
                html.Div(
                    className='div-data',
                    children=[
                        # In-browser storage of global variables
                        html.Div(id="data-df", style={"display": "none"}),
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dcc.Loading(
                                            id="loading-graph",
                                            type="default",
                                            children=[
                                                html.Div(
                                                    className='div-graph',
                                                    id='div-graph',
                                                    children=[],
                                                ),
                                            ]
                                        )
                                    ],
                                )
                            ],
                            align="stretch",
                        ),
                        html.Hr(),
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    children=[
                                        dcc.Loading(
                                            id="loading-table",
                                            type="default",
                                            children=[
                                                html.Div(
                                                    className='div-table',
                                                    id='div-table',
                                                    children=[],
                                                )
                                            ]
                                        )
                                    ],
                                    align='stretch',
                                )
                            ],
                            align="flex-end",
                        )
                    ]
                ),
                fluid=True,
            )
        ]
    )

    return layout
