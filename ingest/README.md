# EPC API Data Download Script

## Set-up

This has been tested on Ubuntu 18.10 - installation on other systems may require some changes.

```
sudo pip3 install requests pandas python-dotenv
```

In order to make calls to the EPC API, the `EPC_API_USER` and `EPC_API_KEY` environment variables are needed. You can either set these variables or create a `.env` file in the directory of this project, with the above variables defined.
For example:
```
EPC_API_USER=<YOUR_API_USER>
EPC_API_KEY=<YOUR_API_KEY>
```
These credentials need to be obtained by registering at https://epc.opendatacommunities.org/login

## Usage

To run the example usage:
```
python3 main.py
```

To import the package from source files in the local directory:
```
import epc_ingest.epc as epc

# epc.search(...)
```