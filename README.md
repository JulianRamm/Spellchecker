# Spellchecker

This is a serverless project, refer to the [serverless installation guide](https://www.serverless.com/framework/docs/providers/aws/guide/installation/) to resolve the requirements needed to run this project. It is not needed that the project is deployed to the cloud. It is enough that the project runs locally, please use the [serverless offline plugin](https://www.npmjs.com/package/serverless-offline) to achieve this.

Once everything is setup correctly. You should be able to run:

```bash
$ serverless offline
```

And get something like this:

```bash
offline: Starting Offline: dev/us-east-1.
offline: Offline [http for lambda] listening on http://localhost:3002
offline: Function names exposed for local invocation by aws-sdk:
           * spellcheck: backend-dev-spellcheck
           * request_history: backend-dev-request_history

   ┌───────────────────────────────────────────────────────────────────────────────────┐
   │                                                                                   │
   │   POST | http://localhost:3000/dev/spellcheck                                     │
   │   POST | http://localhost:3000/2015-03-31/functions/spellcheck/invocations        │
   │   GET  | http://localhost:3000/dev/request_history                                │
   │   POST | http://localhost:3000/2015-03-31/functions/request_history/invocations   │
   │                                                                                   │
   └───────────────────────────────────────────────────────────────────────────────────┘

offline: [HTTP] server ready: http://localhost:3000 �
offline:
offline: Enter "rp" to replay the last request
```

To test that the endpoint is working correctly use cURL:

```bash
$ curl http://localhost:3000/dev/spellcheck> -X POST -d '{ "text": "un lgar para la hopinion"}'
{ "text" : "un lugar para la opinión" }
```

The front is written using Angular Framework. You will need to have installed the dependencies to run the project. Refer to the Angular documentation: [Setup Angular Environment](https://angular.io/guide/setup-local).
After having Angular installed and configured, run the following command to download the required dependencies for the project:

```bash
npm i
```

To run the project run:

```bash
ng serve
```

You will have a view similar to the following:

![Spellchecker front](https://i.imgur.com/lV6oQ4y.png)
