import epc_ingest.epc as epc


def main():
    # example usage of the script: search for properties
    certificates = epc.search(
        local_authority_code='E07000044', property_type='house')

    print(certificates.shape[0])  # number of rows
    print(certificates.head())  # first five rows
    print(certificates['current-energy-rating'])  # all energy rating values


if __name__ == '__main__':
    main()
