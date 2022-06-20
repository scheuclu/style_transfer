from dataclasses import dataclass

@dataclass
class StyleTransferConfiguration():
    content_image_path: str = None
    style_image_path: str = None
    output_image_dir: str = None
    output_image_name: str = None
    numiter: int = 100
    writeevery: int = 10
    style_weight: int = 100000
    content_weight: int = 10
    content_layers: tuple = ('conv_2', 'conv_3')
    style_layers: tuple  = ('conv_4', 'conv_5')
    optimizer: str = 'LBFGS'


standard_configs = [
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_1",
        numiter=500,
        writeevery=10,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight = 100000,
        content_weight = 10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_2",
        numiter=500,
        writeevery=10,
        content_layers=('conv_2', 'conv_3' 'conv_4'),
        style_layers=('conv_3', 'conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_3",
        numiter=5000,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=100000000,
        content_weight=10,
        optimizer='Adam'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/wood1_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_wood_1",
        numiter=2500,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=100000000,
        content_weight=10,
        optimizer='Adam'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/wood1_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_wood_3",
        numiter=2500,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_3', 'conv_4', 'conv_5'),
        style_weight=100000000,
        content_weight=10,
        optimizer='Adam'
    )#,
    # StyleTransferConfiguration(
    #     content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
    #     style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
    #     output_image_dir="./output",
    #     output_image_name="k_tate_1",
    #     numiter=500,
    #     writeevery=10,
    #     content_layers=('conv_2', 'conv_3'),
    #     style_layers=('conv_4', 'conv_5'),
    #     style_weight=1000000,
    #     content_weight=1,
    #     optimizer='LBFGS'
    # )
    # StyleTransferConfiguration(
    #     content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
    #     style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
    #     output_image_dir="./output",
    #     output_image_name="k_tate_2",
    #     numiter=500,
    #     writeevery=10,
    #     content_layers=('conv_2', 'conv_3' 'conv_4'),
    #     style_layers=('conv_3', 'conv_4', 'conv_5'),
    #     style_weight=1000000,
    #     content_weight=10,
    #     optimizer='LBFGS'
    # ),
    # StyleTransferConfiguration(
    #     content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
    #     style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
    #     output_image_dir="./output",
    #     output_image_name="k_tate_3",
    #     numiter=5000,
    #     writeevery=20,
    #     content_layers=('conv_2', 'conv_3'),
    #     style_layers=('conv_4', 'conv_5'),
    #     style_weight=100000000,
    #     content_weight=10,
    #     optimizer='Adam'
    # )
]

