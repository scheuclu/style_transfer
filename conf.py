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
    content_weight: int = 10,
    content_layers: tuple = ('conv_2', 'conv_3')
    style_layers: tuple  = ('conv_4', 'conv_5')
    optimizer: str = 'Adam'


standard_configs = [
    # StyleTransferConfiguration(
    #     content_image_path = "./data/images/content/kayleigh_beach1_1200x800.jpg",
    #     style_image_path = "./data/images/neural-style/mona_1200x800.jpg",
    #     output_image_dir = "./output",
    #     output_image_name = "kayleigh_mona_lisa_1",
    #     numiter = 100,
    #     writeevery = 10
    # )
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_4",
        numiter=100,
        writeevery=10
    )
]

