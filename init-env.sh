#!/bin/bash

# Make sure to run this as source ./init-env.sh

# Path to your YAML file
YAML_FILE="config.yaml"

# Read each key-value pair and export it as an environment variable
while IFS= read -r line; do
  key=$(echo "$line" | cut -f1 -d '=')
  value=$(echo "$line" | cut -f2 -d '=')
  # Use eval to properly handle values with spaces or special characters
  eval export $key=\"$value\"
done < <(yq e '. as $object | to_entries | .[] | .key + "=" + (.value | tostring)' $YAML_FILE)

# Example of how to use the newly set environment variables
# echo $YOUR_VARIABLE_NAME