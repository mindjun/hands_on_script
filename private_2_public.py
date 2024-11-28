from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


private_content = '''-----BEGIN PRIVATE KEY-----
MIGTAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBHkwdwIBAQQgzBwoNAGAT/fZn4iZ
qbdBNicbAuxEvlmdvmZMFZZr6LGgCgYIKoZIzj0DAQehRANCAAQ8ytcK1PI2BFLb
+epKgnKVZ4ZHhTvrEWiott4HWkS5saZiXpWiHfSGpslqgzgQVmypm4UCY3IIw1TC
dUgAattd
-----END PRIVATE KEY-----
'''
# 加载私钥
private_key = serialization.load_pem_private_key(
        private_content.encode('utf-8'),
        password=None,
        backend=default_backend()
    )

# 生成公钥
public_key = private_key.public_key()

pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pem.decode('utf-8'))

# 保存公钥到文件
# with open("public_key.pem", "wb") as public_key_file:
#     public_key_file.write(
#         public_key.public_bytes(
#             encoding=serialization.Encoding.PEM,
#             format=serialization.PublicFormat.SubjectPublicKeyInfo
#         )
#     )

# print("Public key has been generated and saved as public_key.pem")
