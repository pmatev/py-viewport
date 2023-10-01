#!/bin/bash

# Generate TypeScript bindings
protoc --plugin=protoc-gen-ts=frontend/node_modules/.bin/protoc-gen-ts \
       --ts_out=frontend/ \
       proto/*.proto

# Generate Python bindings
protoc --python_out=viewport/ \
       proto/*.proto
