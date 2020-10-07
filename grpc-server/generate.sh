python3 -m grpc_tools.protoc -I ./protos \
  --python_out=./data_app/autogen \
  --grpc_python_out=./data_app/autogen ./protos/*.proto
echo "Generated in ./data_app/autogen"

sed -i -E 's/^import.*_pb2/from . \0/' ./data_app/autogen/*.py

if [ $# -eq 0 ]
  then
    echo -e "Folder path not supplied. So, no copying"
    echo "Folder path example: ../rest-server/app"
else
cp -r ./data_app/autogen $1
echo "Copied to ${1}/autogen"
fi

