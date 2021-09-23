import click


@click.command()
@click.option("-f", "--config", default="config/arguments.py", help="Path to the configuration file. Defaults to config/arguments.py")
def main(config):
    '''
    Utility for pulling data from a WebDav server, compressing data, and moving snapshot to cold storage
    '''
    print(config)


if __name__ == "__main__":
    main()
