import io
from django.core.files.uploadedfile import InMemoryUploadedFile

def combine_uploaded_files(uploaded_files_list):
    # print(uploaded_files_list)
    # # Create an empty list to hold the content of individual uploaded files
    content_list = []

    # # Iterate through the list of uploaded files and read their content
    # for uploaded_file in uploaded_files_list:
    #     # Read the content from each uploaded file and append it to the content_list
    #     content_list.append(uploaded_file.read())
    content_list.append('/home/sunder/Pictures/sunder.PNG'.read())
    print(content_list)
    # # Join the contents from all uploaded files into a single bytes object
    # combined_content = b"".join(content_list)

    # # Create a new in-memory file-like object using BytesIO with the combined content
    # combined_in_memory_file = io.BytesIO(combined_content)

    # # Create a new Django UploadedFile object using the combined in-memory file
    # combined_uploaded_file = InMemoryUploadedFile(
    #     combined_in_memory_file,
    #     field_name='file',  # Replace 'file' with the name of the field in your model
    #     name='combined_file.txt',  # Set the desired name for the combined file
    #     content_type='application/octet-stream',  # Set the appropriate content type
    #     size=len(combined_content),
    #     charset=None
    # )

    # # Return the combined Django UploadedFile object
    # print(combined_uploaded_file)
image_paths=['/home/sunder/Pictures/sunder.PNG','/home/sunder/Pictures/sunder.PNG']
combined_uploaded_file = combine_uploaded_files(image_paths)