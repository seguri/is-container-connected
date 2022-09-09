#!/bin/sh

NAME="is-container-connected"
docker run -d --name "$NAME" -p 8080:80 "$NAME"
