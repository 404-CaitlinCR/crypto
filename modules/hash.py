import hashlib

# text = "Hello World!"
# hash_object = hashlib.sha256(text.encode())
# hash_digest = hash_object.hexdigest()
# print("SHA hash of our ", text, "is ", hash_digest)


def hash_file(file_path):
    #create a hash object, saying we want to use the sha256 algorithm
    h = hashlib.new("sha256")

    #open the file
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(1024)
            if chunk == b"": #exit when empty
                break
            h.update(chunk)
    return h.hexdigest()

def verify_integrety(file1, file2):
    hash1 = hash_file(file1) #verify file one
    hash2 = hash_file(file2) #verify file 2
    print("\n checking inegreity between ", file1," and ", file2)
    if hash1 == hash2:
        return "file is intact"
    return "file has be modified"

#testing
if __name__ == "__main__":
    print("SHA Hash of file is: ", hash_file("/mnt/c/Users/caitl/Desktop/learnCryptography/crypto/sample_files/sample.txt"))