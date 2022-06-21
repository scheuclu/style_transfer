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
        style_weight=1000000,
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
        style_weight=1000000,
        content_weight=10,
        optimizer='Adam'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_tate_1x",
        numiter=500,
        writeevery=10,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=1,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_tate_2x",
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
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_tate_3x",
        numiter=5000,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=100000000,
        content_weight=10,
        optimizer='Adam'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_mona_1",
        numiter=500,
        writeevery=10,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=100000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_mona_2",
        numiter=500,
        writeevery=10,
        content_layers=('conv_2', 'conv_3' 'conv_4'),
        style_layers=('conv_3', 'conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_mona_3",
        numiter=5000,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=100000000,
        content_weight=10,
        optimizer='Adam'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/wood1_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_wood_1",
        numiter=2500,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='Adam'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/wood1_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_wood_3",
        numiter=2500,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_3', 'conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='Adam'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_tate_1x",
        numiter=500,
        writeevery=10,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=1,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_tate_2x",
        numiter=500,
        writeevery=10,
        content_layers=('conv_2', 'conv_3' 'conv_4'),
        style_layers=('conv_3', 'conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_tate_3x",
        numiter=5000,
        writeevery=20,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=100000000,
        content_weight=10,
        optimizer='Adam'
    )
]

scream_configs = [
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_tate_5",
        numiter=400,
        writeevery=10,
        content_layers=('conv_3', 'conv_4'),
        style_layers=('conv_3', 'conv_4'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_scream_1",
        numiter=400,
        writeevery=10,
        content_layers=('conv_2', 'conv_3', 'conv_4'),
        style_layers=('conv_3', 'conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_scream_2",
        numiter=400,
        writeevery=10,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_scream_3",
        numiter=400,
        writeevery=10,
        content_layers=('conv_3', 'conv_4'),
        style_layers=('conv_3', 'conv_4'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_scream_4",
        numiter=400,
        writeevery=10,
        content_layers=('conv_2', 'conv_3', 'conv_4'),
        style_layers=('conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/Tate_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_tate_5",
        numiter=400,
        writeevery=10,
        content_layers=('conv_3', 'conv_4'),
        style_layers=('conv_3', 'conv_4'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_scream_1",
        numiter=400,
        writeevery=10,
        content_layers=('conv_2', 'conv_3', 'conv_4'),
        style_layers=('conv_3', 'conv_4', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_scream_2",
        numiter=400,
        writeevery=10,
        content_layers=('conv_2', 'conv_3'),
        style_layers=('conv_4', 'conv_5'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_scream_3",
        numiter=400,
        writeevery=10,
        content_layers=('conv_3', 'conv_4'),
        style_layers=('conv_3', 'conv_4'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/scream_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_scream_4",
        numiter=400,
        writeevery=10,
        content_layers=('conv_2', 'conv_3', 'conv_4'),
        style_layers=('conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    )
]



# Gogh configs
gogh_configs = [
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_gogh_1",
        numiter=200,
        writeevery=10,
        content_layers=('conv_9', 'conv_14'),
        style_layers=('conv_5', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_gogh_2",
        numiter=200,
        writeevery=10,
        content_layers=('conv_13', 'conv_14'),
        style_layers=('conv_2', 'conv_4', 'conv_8'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_gogh_3",
        numiter=200,
        writeevery=10,
        content_layers=('conv_15', 'conv_10'),
        style_layers=('conv_7', 'conv_6'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_gogh_4",
        numiter=200,
        writeevery=10,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_6'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_gogh_1",
        numiter=200,
        writeevery=10,
        content_layers=('conv_12', 'conv_14'),
        style_layers=('conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_gogh_2",
        numiter=200,
        writeevery=10,
        content_layers=('conv_12'),
        style_layers=('conv_4'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_gogh_3",
        numiter=200,
        writeevery=10,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_8'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/gogh_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_gogh_4",
        numiter=200,
        writeevery=10,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_10'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    )
]


# Gogh configs
klimt_configs = [
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_klimt_1",
        numiter=200,
        writeevery=10,
        content_layers=('conv_9', 'conv_14'),
        style_layers=('conv_5', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_klimt_2",
        numiter=200,
        writeevery=10,
        content_layers=('conv_13', 'conv_14'),
        style_layers=('conv_2', 'conv_4', 'conv_8'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_klimt_3",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_10'),
        style_layers=('conv_7', 'conv_6'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_klimt_4",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_6'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_klimt_1",
        numiter=200,
        writeevery=5,
        content_layers=('conv_12', 'conv_14'),
        style_layers=('conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_klimt_2",
        numiter=200,
        writeevery=5,
        content_layers=('conv_12'),
        style_layers=('conv_4'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_klimt_3",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_8'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/klimt_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_klimt_4",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_10'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    )
]

mona_configs = [
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_mona_1",
        numiter=200,
        writeevery=10,
        content_layers=('conv_9', 'conv_14'),
        style_layers=('conv_5', 'conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_mona_2",
        numiter=200,
        writeevery=10,
        content_layers=('conv_13', 'conv_14'),
        style_layers=('conv_2', 'conv_4', 'conv_8'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_mona_3",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_10'),
        style_layers=('conv_7', 'conv_6'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/couple.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="couple_mona_4",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_6'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_1",
        numiter=200,
        writeevery=5,
        content_layers=('conv_12', 'conv_14'),
        style_layers=('conv_5'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_2",
        numiter=200,
        writeevery=5,
        content_layers=('conv_12'),
        style_layers=('conv_4'),
        style_weight=10000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_3",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_8'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    ),
    StyleTransferConfiguration(
        content_image_path="./data/images/content/kayleigh_beach1_1200x800.jpg",
        style_image_path="./data/images/neural-style/mona_1200x800.jpg",
        output_image_dir="./output",
        output_image_name="k_mona_4",
        numiter=200,
        writeevery=5,
        content_layers=('conv_15', 'conv_16'),
        style_layers=('conv_2', 'conv_10'),
        style_weight=1000000,
        content_weight=10,
        optimizer='LBFGS'
    )
]


