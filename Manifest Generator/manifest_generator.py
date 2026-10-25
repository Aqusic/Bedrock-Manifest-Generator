import uuid
print("""Manifest Generator
v1.0-beta
Format Version 2""")

packname=input("Enter pack name>")
packdesc=input("Enter pack description>")

uuida=uuid.uuid4()
uuidb=uuid.uuid4()

print('''{
    "format_version": 2,
    "header": {
        "description": "''',packdesc,'''",
        "name": "''',packname,'''",
        "uuid": "''',uuida,'''",
        "pack_scope": "world",
        "version": [1, 0, 0],
        "min_engine_version": [1, 20, 0]
    },
    "modules": [
        {
            "description": "''',packdesc,'''",
            "type": "resources",
            "uuid": "''',uuidb,'''",
            "version": [1, 0, 0]
        }
    ]
}''',sep="")
