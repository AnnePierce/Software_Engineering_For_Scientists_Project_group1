#!usr/bin/python3
"""
write stuff
"""
import parsing as ps
import Plotting as pt
import functions as fn


def input_parser():
    """
    add func doc string
    """
    counter_inputs = 0
    my_parser = argparse.ArgumentParser()

    my_parser.add_argument(
        '-c',
        '--config',
        type=str,
        action='store',
        help="This option allows you to specify a config file.",
        required=False
    )


    # Parse command line arguments
    counter_inputs = my_parser.parse_args()

    return counter_inputs


def main():

    # process the file arguments
    my_args = input_parser()

    (my_args.config is not None):  # config has precedence over args.
    my_config = configparser.ConfigParser()
    my_config.read(my_args.config)
    file_name = my_config['FILES']['input']
    column_number = int(my_config['COLS']['state_column'])
    start_year = int(my_config['FILTERS']['start_year'])
    end_year = int(my_config['FILTERS']['end_year'])


if __name__ == "__main__":
    main()