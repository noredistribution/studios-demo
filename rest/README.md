# REST API examples

## cURL examples

### Create a workspace

```shell
curl -L -X POST "https://cvp1/api/resources/workspace/v1/WorkspaceConfig" -H "Content-Type: application/json" -H "Authorization: Bearer `cat token.tok`" -d @ws.json
```

### Query input stats

> NOTE this has to be done in the mainline

```shell
curl -L -X GET "https://cvp1/api/resources/studio/v1/Inputs?key.studioId=bf40ee48-7fa0-4347-a7b4-5a8d794943e7&key.workspaceId=&key.path.values=sites&key.path.values=1&key.path.values=inputs&key.path.values=sitesGroup&key.path.values=devices&key.path.values=0&key.path.values=inputs&key.path.values=devicesGroup&key.path.values=interfaceRanges&key.path.values=8" -H "Authorization: Bearer `cat token.tok`"
```

### Set new inputs

```shell
curl -L -X POST "https://cvp1/api/resources/studio/v1/InputsConfig/some" -H "Content-Type: application/json" -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.`cat token.tok`" -d @input_config_1.json
```

```shell
curl -L -X POST "https://cvp1/api/resources/studio/v1/InputsConfig/some" -H "Content-Type: application/json" -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.`cat token.tok`" -d @input_config_2.json
```

```shell
curl -L -X POST "https://cvp1/api/resources/studio/v1/InputsConfig/some" -H "Content-Type: application/json" -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.`cat token.tok`" -d @evpn_partial.json
```

### Start Build for the workspace

```shell
curl -L -X POST "https://cvp1/api/resources/workspace/v1/WorkspaceConfig" -H "Content-Type: application/json" -H "Authorization: Bearer `cat token.tok`" -d @ws_start_build.json
```

### Submit Build for the workspace

```shell
curl -L -X POST "https://cvp1/api/resources/workspace/v1/WorkspaceConfig" -H "Content-Type: application/json" -H "Authorization: Bearer `cat token.tok`" -d @ws_submit.json
```

> LPT: For setting partial inputs always take a look at the full inputs and work your way down until the specific key you want to update.

## Postman examples

The easiest way to test and use resource APIs with Postman is to import the swagger files into Postman Collections

For studios the 4 main collections used are:

- [tag.v2](https://github.com/aristanetworks/cloudvision-apis/blob/trunk/arista/tag.v2/services.gen.swagger.json)
- [workspace.v1](https://github.com/aristanetworks/cloudvision-apis/blob/trunk/arista/workspace.v1/services.gen.swagger.json)
- [studio.v1](https://github.com/aristanetworks/cloudvision-apis/blob/trunk/arista/studio.v1/services.gen.swagger.json)
- [changecontrol.v1](https://github.com/aristanetworks/cloudvision-apis/blob/trunk/arista/changecontrol.v1/services.gen.swagger.json)

### Example

`POST /api/resources/workspace/v1/WorkspaceConfig`

![create_workspace](./media/create_ws.png)

`GET /api/resources/studio/v1/Inputs?key.studioId={{studioId}}&key.workspaceId=&key.path.values={{value1}}&key.path.values={{value2}}`

![get_partial_inputs](./media/get_partial_inputs.png)

`POST /api/resources/studio/v1/InputsConfig/some`

![set_partial_inputs](./media/set_partial_inputs.png)

`POST /api/resources/workspace/v1/WorkspaceConfig`

![build_ws](./media/build_ws.png)

`POST /api/resources/workspace/v1/WorkspaceConfig`

![submit_Ws](./media/submit_ws.png)
