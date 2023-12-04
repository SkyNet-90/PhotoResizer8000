# PhotoResizer8000

PhotoResizer8000 is an Azure Function that automatically resizes JPEG and PNG images uploaded to a specific Azure Blob Storage container.

## Features

- Listens for new blobs in the 'images' container
- Resizes JPEG and PNG images to a maximum size of 800x800 while maintaining aspect ratio
- Writes the resized image back to Blob Storage

## Prerequisites

- Azure account
- Azure Storage account
- Azure Functions Core Tools
- Python 3.6 or later
- Pillow library for Python

## Local Development

1. Clone this repository to your local machine.
2. Navigate to the function app directory.
3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Start the function app locally:

    ```bash
    func start
    ```

## Deployment to Azure

1. Create a new function app in the Azure portal.
2. Set the `AzureWebJobsStorage` application setting to the connection string of your Azure Storage account.
3. Deploy the function app:

    ```bash
    func azure functionapp publish YOUR_FUNCTION_APP_NAME
    ```

Replace `YOUR_FUNCTION_APP_NAME` with the name of your function app.

## Usage

1. Upload a JPEG or PNG image to the 'images' container in your Azure Storage account.
2. The function will automatically resize the image and write it back to Blob Storage.