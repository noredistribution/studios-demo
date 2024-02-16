# REST API examples

## Create a workspace

```shell
curl -L -X POST "https://cvp1/api/resources/workspace/v1/WorkspaceConfig" -H "Content-Type: application/json" -H "Authorization: Bearer `cat token.tok`" -d @ws.json
```

## Query input stats

> NOTE this has to be done in the mainline

```shell
curl -L -X GET "https://cvp1/api/resources/studio/v1/Inputs?key.studioId=bf40ee48-7fa0-4347-a7b4-5a8d794943e7&key.workspaceId=&key.path.values=sites&key.path.values=1&key.path.values=inputs&key.path.values=sitesGroup&key.path.values=devices&key.path.values=0&key.path.values=inputs&key.path.values=devicesGroup&key.path.values=interfaceRanges&key.path.values=8" -H "Authorization: Bearer `cat token.tok`"
```

## Set new inputs

```shell
curl -L -X POST "https://cvp1/api/resources/studio/v1/InputsConfig/some" -H "Content-Type: application/json" -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.`cat token.tok`" -d @input_config_1.json
```

```shell
curl -L -X POST "https://cvp1/api/resources/studio/v1/InputsConfig/some" -H "Content-Type: application/json" -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.`cat token.tok`" -d @input_config_2.json
```

## Start Build for the workspace

```shell
curl -L -X POST "https://cvp1/api/resources/workspace/v1/WorkspaceConfig" -H "Content-Type: application/json" -H "Authorization: Bearer `cat token.tok`" -d @ws_start_build.json
```

## Submit Build for the workspace

```shell
curl -L -X POST "https://cvp1/api/resources/workspace/v1/WorkspaceConfig" -H "Content-Type: application/json" -H "Authorization: Bearer `cat token.tok`" -d @ws_submit.json
```
