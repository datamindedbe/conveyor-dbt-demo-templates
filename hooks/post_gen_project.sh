#! /usr/bin/env bash

set -eu
shopt -s dotglob
mv * ..
rm -fr ../{{ cookiecutter.project_name }}
cp ./../target/manifest.json ./../dags/manifest.json