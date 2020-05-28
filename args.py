import argparse


def Parse():
    parser = argparse.ArgumentParser(
        description='This app turns GPS coords into URL of a specific maps provider')
    parser.add_argument('--latitude',
                        help='latitude', required=True)
    parser.add_argument('--longitude',
                        help='longitude', required=True)
    parser.add_argument(
        '-m', '--map', help='map provider. Can me google, osm, yandex, bing, waze')

    args = parser.parse_args()
    return args
