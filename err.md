
D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\bin>kibana
node:internal/modules/cjs/loader:1404
  throw err;
  ^

Error: Cannot find module 'D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\dist'
    at Function._resolveFilename (node:internal/modules/cjs/loader:1401:15)
    at defaultResolveImpl (node:internal/modules/cjs/loader:1057:19)
    at resolveForCJSWithHooks (node:internal/modules/cjs/loader:1062:22)
    at Function._load (node:internal/modules/cjs/loader:1211:37)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)
    at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:171:5)
    at node:internal/main/run_main_module:36:49 {
  code: 'MODULE_NOT_FOUND',
  requireStack: []
}

Node.js v22.17.1

D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\bin>kibana
{"log.level":"info","@timestamp":"2025-10-07T16:55:39.157Z","log.logger":"elastic-apm-node","ecs.version":"8.10.0","agentVersion":"4.13.0","env":{"pid":3848,"proctitle":"C:\\Windows\\System32\\cmd.exe - kibana","os":"win32 10.0.22621","arch":"x64","host":"zss","timezone":"UTC+0800","runtime":"Node.js v22.17.1"},"config":{"active":{"source":"start","value":true},"breakdownMetrics":{"source":"start","value":false},"captureBody":{"source":"start","value":"off","commonName":"capture_body"},"captureHeaders":{"source":"start","value":false},"centralConfig":{"source":"start","value":false},"contextPropagationOnly":{"source":"start","value":true},"environment":{"source":"start","value":"production"},"globalLabels":{"source":"start","value":[["git_rev","a8042692500503cca8f3d4aed3c38da398c22f9d"]],"sourceValue":{"git_rev":"a8042692500503cca8f3d4aed3c38da398c22f9d"}},"logLevel":{"source":"default","value":"info","commonName":"log_level"},"metricsInterval":{"source":"start","value":120,"sourceValue":"120s"},"serverUrl":{"source":"start","value":"https://kibana-cloud-apm.apm.us-east-1.aws.found.io/","commonName":"server_url"},"transactionSampleRate":{"source":"start","value":0.1,"commonName":"transaction_sample_rate"},"captureSpanStackTraces":{"source":"start","sourceValue":false},"secretToken":{"source":"start","value":"[REDACTED]","commonName":"secret_token"},"serviceName":{"source":"start","value":"kibana","commonName":"service_name"},"serviceVersion":{"source":"start","value":"9.1.4","commonName":"service_version"}},"activationMethod":"require","message":"Elastic APM Node.js Agent v4.13.0"}
Native global console methods have been overridden in production environment.
[2025-10-08T00:55:45.066+08:00][INFO ][root] Kibana is starting
[2025-10-08T00:55:45.091+08:00][INFO ][node] Kibana process configured with roles: [background_tasks, ui]
[2025-10-08T00:55:55.538+08:00][INFO ][plugins-service] The following plugins are disabled: "cloudChat,cloudExperiments,cloudFullStory,dataUsage,onechat,profilingDataAccess,profiling,securitySolutionServerless,serverless,serverlessObservability,serverlessSearch".
[2025-10-08T00:55:55.604+08:00][INFO ][http.server.Preboot] http server running at http://localhost:5601
[2025-10-08T00:55:55.680+08:00][INFO ][plugins-system.preboot] Setting up [1] plugins: [interactiveSetup]
[2025-10-08T00:55:55.727+08:00][INFO ][preboot] "interactiveSetup" plugin is holding setup: Validating Elasticsearch connection configuration…
[2025-10-08T00:55:56.026+08:00][INFO ][root] Holding setup until preboot stage is completed.


i Kibana has not been configured.

Go to http://localhost:5601/?code=511110 to get started.


[2025-10-08T00:56:45.907+08:00][INFO ][cli] Reloading Kibana configuration (reason: configuration might have changed during preboot stage).
[2025-10-08T00:56:45.914+08:00][INFO ][cli] Reloaded Kibana configuration (reason: configuration might have changed during preboot stage).
[2025-10-08T00:56:45.970+08:00][WARN ][config.deprecation] TLS is not enabled, or the HTTP protocol is set to HTTP/1. Enabling TLS and using HTTP/2 improves security and performance.
[2025-10-08T00:56:46.167+08:00][INFO ][plugins-system.standard] Setting up [171] plugins: [devTools,translations,screenshotMode,usageCollection,telemetryCollectionManager,telemetryCollectionXpack,kibanaUsageCollection,contentManagement,cloud,intercepts,productIntercept,newsfeed,savedObjectsFinder,noDataPage,monitoringCollection,licensing,taskManager,share,productDocBase,indicesMetadata,mapsEms,globalSearch,globalSearchProviders,features,guidedOnboarding,banners,licenseApiGuard,customBranding,ftrApis,fieldsMetadata,fieldFormats,expressions,screenshotting,dataViews,esUiShared,customIntegrations,home,searchprofiler,painlessLab,management,spaces,security,telemetry,licenseManagement,snapshotRestore,lists,files,encryptedSavedObjects,taskManagerDependencies,entityManager,eventLog,actions,notifications,inference,observabilityAIAssistant,llmTasks,advancedSettings,data,savedObjectsTagging,globalSearchBar,savedObjectsManagement,unifiedSearch,navigation,inferenceEndpoint,graph,embeddable,uiActionsEnhanced,dashboardEnhanced,savedSearch,presentationUtil,controls,alerting,logsDataAccess,fileUpload,ecsDataQualityDashboard,dataViewFieldEditor,dataViewManagement,console,searchSynonyms,searchQueryRules,searchNotebooks,searchHomepage,ingestPipelines,charts,watcher,visualizations,visTypeXy,visTypeVislib,visTypeVega,visTypeTimeseries,visTypeTimelion,visTypeTagcloud,visTypeTable,visTypeMetric,visTypeMarkdown,visTypeHeatmap,inputControlVis,expressionTagcloud,expressionPartitionVis,visTypePie,expressionMetricVis,expressionLegacyMetricVis,expressionHeatmap,expressionGauge,visTypeGauge,eventAnnotation,expressionXY,lens,maps,dataVisualizer,dashboard,triggersActionsUi,transform,stackConnectors,automaticImport,stackAlerts,ruleRegistry,streams,cases,timelines,sessionView,metricsDataAccess,aiops,links,logsShared,upgradeAssistant,apmSourcesAccess,discover,reporting,canvas,ml,searchPlayground,searchInferenceEndpoints,searchAssistant,observabilityAiAssistantManagement,fleet,osquery,monitoring,logstash,indexManagement,searchIndices,rollup,remoteClusters,crossClusterReplication,indexLifecycleManagement,esql,contentConnectors,enterpriseSearch,datasetQuality,streamsApp,dataQuality,cloudSecurityPosture,exploratoryView,observability,uptime,slo,synthetics,observabilityLogsExplorer,discoverEnhanced,apmDataAccess,infra,apm,ux,observabilityOnboarding,cloudDataMigration,aiAssistantManagementSelection,observabilityAIAssistantApp,elasticAssistant,securitySolution,securitySolutionEss,grokdebugger]
[2025-10-08T00:56:47.300+08:00][INFO ][plugins.taskManager] TaskManager is identified by the Kibana UUID: b98548d3-69d5-43a6-8d43-b43726c0b598
[2025-10-08T00:56:47.489+08:00][INFO ][custom-branding-service] CustomBrandingService registering plugin: customBranding
[2025-10-08T00:56:48.588+08:00][INFO ][plugins.screenshotting.config] Chromium sandbox provides an additional layer of protection, and is supported for Win32 OS. Automatically enabling Chromium sandbox.
[2025-10-08T00:56:49.118+08:00][WARN ][plugins.security.config] Generating a random key for xpack.security.encryptionKey. To prevent sessions from being invalidated on restart, please set xpack.security.encryptionKey in the kibana.yml or use the bin/kibana-encryption-keys command.
[2025-10-08T00:56:49.119+08:00][INFO ][plugins.security.config] Hashed 'xpack.security.encryptionKey' for this instance: T6EpL5Rui6gc7i632NRj1JEHXpU/zkT+/aNc5qWa/g8=
[2025-10-08T00:56:49.120+08:00][WARN ][plugins.security.config] Session cookies will be transmitted over insecure connections. This is not recommended.
[2025-10-08T00:56:49.167+08:00][WARN ][plugins.security.config] Generating a random key for xpack.security.encryptionKey. To prevent sessions from being invalidated on restart, please set xpack.security.encryptionKey in the kibana.yml or use the bin/kibana-encryption-keys command.
[2025-10-08T00:56:49.168+08:00][INFO ][plugins.security.config] Hashed 'xpack.security.encryptionKey' for this instance: kC81Ia7M2AVI62hQsJGVSrUzjKBhmZi9KIBuWf7n5o0=
[2025-10-08T00:56:49.168+08:00][WARN ][plugins.security.config] Session cookies will be transmitted over insecure connections. This is not recommended.
[2025-10-08T00:56:49.816+08:00][WARN ][plugins.encryptedSavedObjects] Saved objects encryption key is not set. This will severely limit Kibana functionality. Please set xpack.encryptedSavedObjects.encryptionKey in the kibana.yml or use the bin/kibana-encryption-keys command.
[2025-10-08T00:56:50.124+08:00][WARN ][plugins.actions] APIs are disabled because the Encrypted Saved Objects plugin is missing encryption key. Please set xpack.encryptedSavedObjects.encryptionKey in the kibana.yml or use the bin/kibana-encryption-keys command.
[2025-10-08T00:56:50.173+08:00][INFO ][plugins.notifications] Email Service Error: Email connector not specified.
[2025-10-08T00:56:50.734+08:00][WARN ][plugins.alerting] APIs are disabled because the Encrypted Saved Objects plugin is missing encryption key. Please set xpack.encryptedSavedObjects.encryptionKey in the kibana.yml or use the bin/kibana-encryption-keys command.
[2025-10-08T00:56:50.736+08:00][INFO ][plugins.alerting] using indexes and aliases for persisting alerts
[2025-10-08T00:56:53.850+08:00][INFO ][root] Kibana is shutting down
[2025-10-08T00:56:53.856+08:00][FATAL][root] Reason: Cannot find module '../series_functions/undefined'
Require stack:
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\lib\load_functions.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\plugin.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugin.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\discovery\plugins_discovery.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\discovery\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugins_service.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\server.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core\server\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\serve\serve.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\cli.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\dist.js
Error: Cannot find module '../series_functions/undefined'
Require stack:
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\lib\load_functions.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\plugin.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugin.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\discovery\plugins_discovery.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\discovery\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugins_service.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\server.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core\server\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\serve\serve.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\cli.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\dist.js
    at Function._resolveFilename (node:internal/modules/cjs/loader:1401:15)
    at defaultResolveImpl (node:internal/modules/cjs/loader:1057:19)
    at resolveForCJSWithHooks (node:internal/modules/cjs/loader:1062:22)
    at Function._load (node:internal/modules/cjs/loader:1211:37)
    at TracingChannel.traceSync (node:diagnostics_channel:322:14)
    at wrapModuleLoad (node:internal/modules/cjs/loader:235:24)
    at Module.<anonymous> (node:internal/modules/cjs/loader:1487:12)
    at Module.patchedRequire (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\require-in-the-middle\index.js:233:34)
    at Module.Hook._require.Module.require (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\require-in-the-middle\index.js:181:27)
    at Module.patchedRequire (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\require-in-the-middle\index.js:233:34)
    at Module.Hook._require.Module.require (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\require-in-the-middle\index.js:181:27)
    at require (node:internal/modules/helpers:135:16)
    at getTuple (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\lib\load_functions.js:22:19)
    at D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\lib\load_functions.js:39:12
    at arrayMap (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:653:23)
    at Function.map (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:9622:14)
    at interceptor (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:17094:35)
    at thru (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:8859:14)
    at D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:4430:28
    at arrayReduce (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:697:21)
    at baseWrapperValue (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:4429:14)
    at LazyWrapper.lazyValue [as value] (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:1901:16)
    at baseWrapperValue (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:4427:25)
    at LodashWrapper.wrapperValue (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\lodash\lodash.js:9114:14)
    at _default (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\lib\load_functions.js:40:6)
    at TimelionPlugin.setup (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\plugin.js:33:51)
    at PluginWrapper.setup (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugin.js:86:26)
    at PluginsSystem.setupPlugins (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugins_system.js:103:40)
    at PluginsService.setup (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugins_service.js:120:19)
    at Server.setup (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\server.js:383:26)
    at Root.setup (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\root\index.js:58:14)
    at bootstrap (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\bootstrap.js:118:5)
    at Command.<anonymous> (D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\serve\serve.js:236:5)
[2025-10-08T00:56:53.901+08:00][INFO ][plugins-system.preboot] Stopping all plugins.
[2025-10-08T00:56:53.902+08:00][INFO ][plugins-system.preboot] All plugins stopped.
[2025-10-08T00:56:53.903+08:00][INFO ][plugins-system.standard] Stopping all plugins.
[2025-10-08T00:56:53.914+08:00][INFO ][plugins-system.standard] All plugins stopped.
[2025-10-08T00:56:54.618+08:00][INFO ][plugins.screenshotting.chromium] Browser executable: D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\screenshotting-plugin\chromium\chrome-headless-shell-win64\chrome-headless-shell.exe

\u001b[37m\u001b[41m FATAL \u001b[49m\u001b[39m Error: Cannot find module '../series_functions/undefined'
Require stack:
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\lib\load_functions.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\plugin.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\vis-type-timelion-plugin\server\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugin.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\discovery\plugins_discovery.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\discovery\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\plugins_service.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\src\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-plugins-server-internal\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\server.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\src\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core-root-server-internal\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\node_modules\@kbn\core\server\index.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\serve\serve.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\cli.js
- D:\software\kibana\download\kibana-9.1.4-windows-x86_64\kibana-9.1.4\src\cli\dist.js

