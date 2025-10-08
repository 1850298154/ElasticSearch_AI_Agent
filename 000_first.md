warning: ignoring JAVA_HOME=D:\java; using bundled JDK
[2025-10-06T03:49:54,399][INFO ][o.e.b.Elasticsearch      ] [ZSS] version[9.1.4], pid[33120], build[zip/0b7fe68d2e369469ff9e9f344ab6df64ab9c5293/2025-09-16T22:05:19.073893347Z], OS[Windows 11/10.0/amd64], JVM[Oracle Corporation/OpenJDK 64-Bit Server VM/24.0.2/24.0.2+12-54]
[2025-10-06T03:49:54,419][INFO ][o.e.b.Elasticsearch      ] [ZSS] JVM home [D:\software\es\download\elasticsearch-9.1.4-windows-x86_64\elasticsearch-9.1.4\jdk], using bundled JDK [true]
[2025-10-06T03:49:54,421][INFO ][o.e.b.Elasticsearch      ] [ZSS] JVM arguments [-Des.networkaddress.cache.ttl=60, -Des.networkaddress.cache.negative.ttl=10, -XX:+AlwaysPreTouch, -Xss1m, -Djava.awt.headless=true, -Dfile.encoding=UTF-8, -Djna.nosys=true, -XX:-OmitStackTraceInFastThrow, -Dio.netty.noUnsafe=true, -Dio.netty.noKeySetOptimization=true, -Dio.netty.recycler.maxCapacityPerThread=0, --add-opens=org.apache.lucene.core/org.apache.lucene.codecs.lucene99=org.elasticsearch.server, --add-opens=org.apache.lucene.backward_codecs/org.apache.lucene.backward_codecs.lucene90=org.elasticsearch.server, --add-opens=org.apache.lucene.backward_codecs/org.apache.lucene.backward_codecs.lucene91=org.elasticsearch.server, --add-opens=org.apache.lucene.backward_codecs/org.apache.lucene.backward_codecs.lucene92=org.elasticsearch.server, --add-opens=org.apache.lucene.backward_codecs/org.apache.lucene.backward_codecs.lucene94=org.elasticsearch.server, --add-opens=org.apache.lucene.backward_codecs/org.apache.lucene.backward_codecs.lucene95=org.elasticsearch.server, -Dlog4j.shutdownHookEnabled=false, -Dlog4j2.disable.jmx=true, -Dlog4j2.formatMsgNoLookups=true, -Djava.locale.providers=CLDR, -Dorg.apache.lucene.vectorization.upperJavaFeatureVersion=24, -Des.path.home=D:\software\es\download\elasticsearch-9.1.4-windows-x86_64\elasticsearch-9.1.4, -Des.distribution.type=zip, -Des.java.type=bundled JDK, --enable-native-access=org.elasticsearch.nativeaccess,org.apache.lucene.core, --enable-native-access=ALL-UNNAMED, --illegal-native-access=deny, -XX:ReplayDataFile=logs/replay_pid%p.log, -Des.entitlements.enabled=true, -XX:+EnableDynamicAgentLoading, -Djdk.attach.allowAttachSelf=true, --patch-module=java.base=D:\software\es\download\elasticsearch-9.1.4-windows-x86_64\elasticsearch-9.1.4\lib\entitlement-bridge\elasticsearch-entitlement-bridge-9.1.4.jar, --add-exports=java.base/org.elasticsearch.entitlement.bridge=org.elasticsearch.entitlement,java.logging,java.net.http,java.naming,jdk.net, -XX:+UseG1GC, -Djava.io.tmpdir=C:\Users\zooos\AppData\Local\Temp\elasticsearch, --add-modules=jdk.incubator.vector, -Dorg.apache.lucene.store.defaultReadAdvice=normal, -XX:+HeapDumpOnOutOfMemoryError, -XX:+ExitOnOutOfMemoryError, -XX:ErrorFile=hs_err_pid%p.log, -Xlog:gc*,gc+age=trace,safepoint:file=gc.log:utctime,level,pid,tags:filecount=32,filesize=64m, -Xms16255m, -Xmx16255m, -XX:MaxDirectMemorySize=8522825728, -XX:InitiatingHeapOccupancyPercent=30, -XX:G1ReservePercent=25, --module-path=D:\software\es\download\elasticsearch-9.1.4-windows-x86_64\elasticsearch-9.1.4\lib, --add-modules=jdk.net, --add-modules=jdk.management.agent, --add-modules=ALL-MODULE-PATH, -Djdk.module.main=org.elasticsearch.server]
[2025-10-06T03:49:54,497][INFO ][o.e.b.Elasticsearch      ] [ZSS] Default Locale [zh_CN]
[2025-10-06T03:49:55,565][INFO ][o.e.n.NativeAccess       ] [ZSS] Using [jdk] native provider and native methods for [Windows]
[2025-10-06T03:49:55,840][INFO ][o.a.l.i.v.PanamaVectorizationProvider] [ZSS] Java vector incubator API enabled; uses preferredBitSize=512; FMA enabled
[2025-10-06T03:49:55,987][INFO ][o.e.b.Elasticsearch      ] [ZSS] Bootstrapping Entitlements
[2025-10-06T03:50:01,429][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [repository-url]
[2025-10-06T03:50:01,430][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [rest-root]
[2025-10-06T03:50:01,430][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-core]
[2025-10-06T03:50:01,431][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-redact]
[2025-10-06T03:50:01,431][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [ingest-user-agent]
[2025-10-06T03:50:01,431][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-async-search]
[2025-10-06T03:50:01,432][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-monitoring]
[2025-10-06T03:50:01,432][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [repository-s3]
[2025-10-06T03:50:01,432][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-analytics]
[2025-10-06T03:50:01,433][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-esql-core]
[2025-10-06T03:50:01,433][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [search-business-rules]
[2025-10-06T03:50:01,433][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-ent-search]
[2025-10-06T03:50:01,434][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-autoscaling]
[2025-10-06T03:50:01,434][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [lang-painless]
[2025-10-06T03:50:01,434][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-ml]
[2025-10-06T03:50:01,435][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [lang-mustache]
[2025-10-06T03:50:01,435][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [legacy-geo]
[2025-10-06T03:50:01,435][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [logsdb]
[2025-10-06T03:50:01,436][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-ql]
[2025-10-06T03:50:01,436][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [rank-rrf]
[2025-10-06T03:50:01,437][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [analysis-common]
[2025-10-06T03:50:01,437][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [health-shards-availability]
[2025-10-06T03:50:01,438][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [transport-netty4]
[2025-10-06T03:50:01,438][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [aggregations]
[2025-10-06T03:50:01,438][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [ingest-common]
[2025-10-06T03:50:01,439][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [frozen-indices]
[2025-10-06T03:50:01,439][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-identity-provider]
[2025-10-06T03:50:01,440][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-shutdown]
[2025-10-06T03:50:01,440][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-text-structure]
[2025-10-06T03:50:01,440][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [snapshot-repo-test-kit]
[2025-10-06T03:50:01,440][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [ml-package-loader]
[2025-10-06T03:50:01,441][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [kibana]
[2025-10-06T03:50:01,441][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [constant-keyword]
[2025-10-06T03:50:01,441][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-logstash]
[2025-10-06T03:50:01,442][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-ccr]
[2025-10-06T03:50:01,442][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-graph]
[2025-10-06T03:50:01,442][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [rank-vectors]
[2025-10-06T03:50:01,442][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-esql]
[2025-10-06T03:50:01,443][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [parent-join]
[2025-10-06T03:50:01,443][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [counted-keyword]
[2025-10-06T03:50:01,443][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-enrich]
[2025-10-06T03:50:01,444][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [repositories-metering-api]
[2025-10-06T03:50:01,444][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [transform]
[2025-10-06T03:50:01,444][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [repository-azure]
[2025-10-06T03:50:01,445][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [dot-prefix-validation]
[2025-10-06T03:50:01,445][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [repository-gcs]
[2025-10-06T03:50:01,445][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [spatial]
[2025-10-06T03:50:01,446][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-otel-data]
[2025-10-06T03:50:01,446][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [apm]
[2025-10-06T03:50:01,446][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [mapper-extras]
[2025-10-06T03:50:01,446][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [mapper-version]
[2025-10-06T03:50:01,447][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-rollup]
[2025-10-06T03:50:01,447][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [percolator]
[2025-10-06T03:50:01,447][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-migrate]
[2025-10-06T03:50:01,448][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [data-streams]
[2025-10-06T03:50:01,448][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-stack]
[2025-10-06T03:50:01,448][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [rank-eval]
[2025-10-06T03:50:01,449][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [reindex]
[2025-10-06T03:50:01,449][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [streams]
[2025-10-06T03:50:01,449][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-security]
[2025-10-06T03:50:01,450][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [blob-cache]
[2025-10-06T03:50:01,450][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [searchable-snapshots]
[2025-10-06T03:50:01,450][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-slm]
[2025-10-06T03:50:01,450][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-geoip-enterprise-downloader]
[2025-10-06T03:50:01,451][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [snapshot-based-recoveries]
[2025-10-06T03:50:01,451][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-watcher]
[2025-10-06T03:50:01,451][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [old-lucene-versions]
[2025-10-06T03:50:01,451][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-ilm]
[2025-10-06T03:50:01,452][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-inference]
[2025-10-06T03:50:01,452][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-voting-only-node]
[2025-10-06T03:50:01,452][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-deprecation]
[2025-10-06T03:50:01,452][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-fleet]
[2025-10-06T03:50:01,453][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-aggregate-metric]
[2025-10-06T03:50:01,458][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-downsample]
[2025-10-06T03:50:01,459][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-profiling]
[2025-10-06T03:50:01,459][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [ingest-geoip]
[2025-10-06T03:50:01,459][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-write-load-forecaster]
[2025-10-06T03:50:01,460][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [ingest-attachment]
[2025-10-06T03:50:01,460][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [wildcard]
[2025-10-06T03:50:01,460][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-apm-data]
[2025-10-06T03:50:01,461][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [unsigned-long]
[2025-10-06T03:50:01,462][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-sql]
[2025-10-06T03:50:01,462][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [runtime-fields-common]
[2025-10-06T03:50:01,463][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-async]
[2025-10-06T03:50:01,463][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [vector-tile]
[2025-10-06T03:50:01,464][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-kql]
[2025-10-06T03:50:01,464][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [lang-expression]
[2025-10-06T03:50:01,465][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [ingest-otel]
[2025-10-06T03:50:01,466][INFO ][o.e.p.PluginsService     ] [ZSS] loaded module [x-pack-eql]
[2025-10-06T03:50:07,048][WARN ][stderr                   ] [ZSS] SLF4J: No SLF4J providers were found.
[2025-10-06T03:50:10,460][WARN ][stderr                   ] [ZSS] SLF4J: Defaulting to no-operation (NOP) logger implementation
[2025-10-06T03:50:10,464][WARN ][stderr                   ] [ZSS] SLF4J: See https://www.slf4j.org/codes.html#noProviders for further details.
[2025-10-06T03:50:11,703][INFO ][o.e.e.NodeEnvironment    ] [ZSS] using [1] data paths, mounts [[鏂板姞鍗?(D:)]], net usable_space [131.8gb], net total_space [1tb], types [NTFS]

[2025-10-06T03:50:11,706][INFO ][o.e.e.NodeEnvironment    ] [ZSS] heap size [15.8gb], compressed ordinary object pointers [true]
[2025-10-06T03:50:12,495][INFO ][o.e.n.Node               ] [ZSS] node name [ZSS], node ID [flAjod6OSo29EiZMhLt6zQ], cluster name [elasticsearch], roles [master, data_warm, data_content, transform, data_hot, ml, data_frozen, ingest, data_cold, data, remote_cluster_client]
[2025-10-06T03:50:15,919][INFO ][o.e.f.FeatureService     ] [ZSS] Registered local node features [ES_V_8, ES_V_9, cluster.reroute.ignores_metric_param, cluster.stats.source_modes, data_stream.failure_store, linear_retriever_supported, lucene_10_1_upgrade, lucene_10_upgrade, security.queryable_built_in_roles, simulate.ignored.fields, snapshots.get.state_parameter]
[2025-10-06T03:50:16,236][INFO ][o.e.i.r.RecoverySettings ] [ZSS] using rate limit [40mb] with [default=40mb, read=0b, write=0b, max=0b]
[2025-10-06T03:50:16,454][INFO ][o.e.c.m.DataStreamGlobalRetentionSettings] [ZSS] Updated global default retention to [null]
[2025-10-06T03:50:16,456][INFO ][o.e.c.m.DataStreamGlobalRetentionSettings] [ZSS] Updated global max retention to [null]
[2025-10-06T03:50:16,457][INFO ][o.e.c.m.DataStreamGlobalRetentionSettings] [ZSS] Updated failures default retention to [30d]
[2025-10-06T03:50:16,458][INFO ][o.e.c.m.DataStreamFailureStoreSettings] [ZSS] Updated data stream name patterns for enabling failure store to [[]]
[2025-10-06T03:50:17,556][INFO ][o.e.x.m.p.l.CppLogMessageHandler] [ZSS] [controller/19232] [Main.cc@123] controller (64 bit): Version 9.1.4 (Build f9253b2bc98598) Copyright (c) 2025 Elasticsearch BV
[2025-10-06T03:50:18,183][INFO ][o.e.x.o.OTelPlugin       ] [ZSS] OTel ingest plugin is enabled
[2025-10-06T03:50:18,238][INFO ][o.e.x.c.t.YamlTemplateRegistry] [ZSS] OpenTelemetry index template registry is enabled
[2025-10-06T03:50:18,265][INFO ][o.e.t.a.APM              ] [ZSS] Sending apm metrics is disabled
[2025-10-06T03:50:18,267][INFO ][o.e.t.a.APM              ] [ZSS] Sending apm tracing is disabled
[2025-10-06T03:50:18,339][INFO ][o.e.x.s.Security         ] [ZSS] Security is enabled
[2025-10-06T03:50:18,940][INFO ][o.e.x.s.a.s.FileRolesStore] [ZSS] parsed [0] roles from file [D:\software\es\download\elasticsearch-9.1.4-windows-x86_64\elasticsearch-9.1.4\config\roles.yml]

[2025-10-06T03:50:19,722][INFO ][o.e.x.w.Watcher          ] [ZSS] Watcher initialized components at 2025-10-05T19:50:19.721Z
[2025-10-06T03:50:20,118][INFO ][o.e.x.p.ProfilingPlugin  ] [ZSS] Profiling is enabled
[2025-10-06T03:50:20,144][INFO ][o.e.x.p.ProfilingPlugin  ] [ZSS] profiling index templates will not be installed or reinstalled
[2025-10-06T03:50:20,202][INFO ][o.e.x.a.APMPlugin        ] [ZSS] APM ingest plugin is enabled
[2025-10-06T03:50:20,268][INFO ][o.e.x.c.t.YamlTemplateRegistry] [ZSS] apm index template registry is enabled
[2025-10-06T03:50:20,980][INFO ][o.e.t.n.NettyAllocator   ] [ZSS] creating NettyAllocator with the following configs: [name=elasticsearch_configured, chunk_size=1mb, suggested_max_allocation_size=1mb, factors={es.unsafe.use_netty_default_chunk_and_page_size=false, g1gc_enabled=true, g1gc_region_size=8mb}]
[2025-10-06T03:50:21,042][INFO ][o.e.d.DiscoveryModule    ] [ZSS] using discovery type [multi-node] and seed hosts providers [settings]
[2025-10-06T03:50:22,804][INFO ][o.e.n.Node               ] [ZSS] initialized
[2025-10-06T03:50:22,805][INFO ][o.e.n.Node               ] [ZSS] starting ...
[2025-10-06T03:50:23,728][INFO ][o.e.x.s.c.f.PersistentCache] [ZSS] persistent cache index loaded
[2025-10-06T03:50:23,730][INFO ][o.e.x.d.l.DeprecationIndexingComponent] [ZSS] deprecation component started
[2025-10-06T03:50:23,972][INFO ][o.e.t.TransportService   ] [ZSS] publish_address {127.0.0.1:9300}, bound_addresses {[::1]:9300}, {127.0.0.1:9300}
[2025-10-06T03:50:24,488][INFO ][o.e.c.c.ClusterBootstrapService] [ZSS] this node has not joined a bootstrapped cluster yet; [cluster.initial_master_nodes] is set to [ZSS]
[2025-10-06T03:50:24,506][INFO ][o.e.c.c.Coordinator      ] [ZSS] setting initial configuration to VotingConfiguration{flAjod6OSo29EiZMhLt6zQ}
[2025-10-06T03:50:24,842][INFO ][o.e.c.s.MasterService    ] [ZSS] elected-as-master ([1] nodes joined in term 1)[_FINISH_ELECTION_, {ZSS}{flAjod6OSo29EiZMhLt6zQ}{f1BOj6vQQ0KiG-vfeEOroA}{ZSS}{127.0.0.1}{127.0.0.1:9300}{cdfhilmrstw}{9.1.4}{8000099-9033000} completing election], term: 1, version: 1, delta: master node changed {previous [], current [{ZSS}{flAjod6OSo29EiZMhLt6zQ}{f1BOj6vQQ0KiG-vfeEOroA}{ZSS}{127.0.0.1}{127.0.0.1:9300}{cdfhilmrstw}{9.1.4}{8000099-9033000}]}
[2025-10-06T03:50:24,913][INFO ][o.e.c.c.CoordinationState] [ZSS] cluster UUID set to [ia4PJ1WiSHCWV1IHjJhEjA]
[2025-10-06T03:50:24,964][INFO ][o.e.c.s.ClusterApplierService] [ZSS] master node changed {previous [], current [{ZSS}{flAjod6OSo29EiZMhLt6zQ}{f1BOj6vQQ0KiG-vfeEOroA}{ZSS}{127.0.0.1}{127.0.0.1:9300}{cdfhilmrstw}{9.1.4}{8000099-9033000}]}, term: 1, version: 1, reason: Publication{term=1, version=1}
[2025-10-06T03:50:25,024][INFO ][o.e.c.c.NodeJoinExecutor ] [ZSS] node-join: [{ZSS}{flAjod6OSo29EiZMhLt6zQ}{f1BOj6vQQ0KiG-vfeEOroA}{ZSS}{127.0.0.1}{127.0.0.1:9300}{cdfhilmrstw}{9.1.4}{8000099-9033000}] with reason [completing election]
[2025-10-06T03:50:25,025][INFO ][o.e.h.AbstractHttpServerTransport] [ZSS] publish_address {192.168.31.58:9200}, bound_addresses {[::]:9200}
[2025-10-06T03:50:25,038][INFO ][o.e.n.Node               ] [ZSS] started {ZSS}{flAjod6OSo29EiZMhLt6zQ}{f1BOj6vQQ0KiG-vfeEOroA}{ZSS}{127.0.0.1}{127.0.0.1:9300}{cdfhilmrstw}{9.1.4}{8000099-9033000}{xpack.installed=true, ml.config_version=12.0.0, ml.max_jvm_size=17045651456, ml.allocated_processors_double=8.0, ml.allocated_processors=8, ml.machine_memory=34089721856, transform.config_version=10.0.0}
[2025-10-06T03:50:25,200][INFO ][o.e.x.m.MlIndexRollover  ] [ZSS] ML legacy indices rolled over
[2025-10-06T03:50:25,201][INFO ][o.e.x.m.MlAnomaliesIndexUpdate] [ZSS] legacy ml anomalies indices rolled over and aliases updated
[2025-10-06T03:50:25,239][INFO ][o.e.c.f.AbstractFileWatchingService] [ZSS] starting file watcher ...
[2025-10-06T03:50:25,253][INFO ][o.e.c.f.AbstractFileWatchingService] [ZSS] file settings service up and running [tid=111]
[2025-10-06T03:50:25,255][INFO ][o.e.r.s.FileSettingsService] [ZSS] setting file [D:\software\es\download\elasticsearch-9.1.4-windows-x86_64\elasticsearch-9.1.4\config\operator\settings.json] not found, initializing [file_settings] as empty
[2025-10-06T03:50:25,277][INFO ][o.e.c.r.a.DiskThresholdMonitor] [ZSS] low disk watermark [85%] exceeded on [flAjod6OSo29EiZMhLt6zQ][ZSS][D:\software\es\download\elasticsearch-9.1.4-windows-x86_64\elasticsearch-9.1.4\data] free: 131.8gb[12.5%], replicas will not be assigned to this node
[2025-10-06T03:50:25,284][INFO ][o.e.x.s.s.SecurityIndexManager] [ZSS] security index does not exist, creating [.security-7] with alias [.security]
[2025-10-06T03:50:25,286][INFO ][o.e.g.GatewayService     ] [ZSS] recovered [0] indices into cluster_state
[2025-10-06T03:50:25,507][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding template [.monitoring-kibana] for index patterns [.monitoring-kibana-7-*]
[2025-10-06T03:50:25,530][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding template [.monitoring-logstash] for index patterns [.monitoring-logstash-7-*]
[2025-10-06T03:50:25,572][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding template [.monitoring-es] for index patterns [.monitoring-es-7-*]
[2025-10-06T03:50:25,603][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding template [.monitoring-beats] for index patterns [.monitoring-beats-7-*]
[2025-10-06T03:50:25,615][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding template [.monitoring-alerts-7] for index patterns [.monitoring-alerts-7]
[2025-10-06T03:50:25,652][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.monitoring-logstash-mb] for index patterns [.monitoring-logstash-8-*]
[2025-10-06T03:50:25,670][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.monitoring-kibana-mb] for index patterns [.monitoring-kibana-8-*]
[2025-10-06T03:50:25,684][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.monitoring-ent-search-mb] for index patterns [.monitoring-ent-search-8-*]
[2025-10-06T03:50:25,708][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [behavioral_analytics-events-mappings]
[2025-10-06T03:50:25,723][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [elastic-connectors-mappings]
[2025-10-06T03:50:25,737][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [elastic-connectors-sync-jobs-mappings]
[2025-10-06T03:50:25,743][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [elastic-connectors-sync-jobs-settings]
[2025-10-06T03:50:25,750][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [elastic-connectors-settings]
[2025-10-06T03:50:25,764][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [search-acl-filter] for index patterns [.search-acl-filter-*]
[2025-10-06T03:50:25,770][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.ml-state] for index patterns [.ml-state*]
[2025-10-06T03:50:25,785][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.ml-notifications-000002] for index patterns [.ml-notifications-*]
[2025-10-06T03:50:25,813][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.monitoring-beats-mb] for index patterns [.monitoring-beats-8-*]
[2025-10-06T03:50:25,840][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.monitoring-es-mb] for index patterns [.monitoring-es-8-*]
[2025-10-06T03:50:25,848][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.ml-stats] for index patterns [.ml-stats-*]
[2025-10-06T03:50:25,870][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.ml-anomalies-] for index patterns [.ml-anomalies-*]
[2025-10-06T03:50:25,875][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [ecs-tsdb@mappings]
[2025-10-06T03:50:25,885][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [otel@mappings]
[2025-10-06T03:50:25,890][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-otel@mappings]
[2025-10-06T03:50:25,919][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces-otel@mappings]
[2025-10-06T03:50:25,925][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [semconv-resource-to-ecs@mappings]
[2025-10-06T03:50:25,940][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs-otel@mappings]
[2025-10-06T03:50:25,942][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [synthetics-settings]
[2025-10-06T03:50:25,946][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs-mappings]
[2025-10-06T03:50:25,949][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-tsdb-settings]
[2025-10-06T03:50:25,953][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-mappings]
[2025-10-06T03:50:25,956][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [synthetics-mappings]
[2025-10-06T03:50:25,959][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-settings]
[2025-10-06T03:50:25,962][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [data-streams-mappings]
[2025-10-06T03:50:25,968][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [ecs@dynamic_templates]
[2025-10-06T03:50:25,970][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces@settings]
[2025-10-06T03:50:25,975][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [agentless@mappings]
[2025-10-06T03:50:25,980][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [data-streams@mappings]
[2025-10-06T03:50:25,987][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics@mappings]
[2025-10-06T03:50:25,992][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [ecs@mappings]
[2025-10-06T03:50:25,996][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [synthetics@mappings]
[2025-10-06T03:50:25,999][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces@mappings]
[2025-10-06T03:50:26,004][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs@mappings]
[2025-10-06T03:50:26,008][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [kibana-reporting@settings]
[2025-10-06T03:50:26,012][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics@tsdb-settings]
[2025-10-06T03:50:26,018][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [agentless@settings]
[2025-10-06T03:50:26,020][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics@settings]
[2025-10-06T03:50:26,024][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [synthetics@settings]
[2025-10-06T03:50:26,032][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.slm-history-7] for index patterns [.slm-history-7*]
[2025-10-06T03:50:26,044][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.watch-history-17] for index patterns [.watcher-history-17*]
[2025-10-06T03:50:26,180][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [ilm-history-7] for index patterns [ilm-history-7*]
[2025-10-06T03:50:26,191][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [.deprecation-indexing-mappings]
[2025-10-06T03:50:26,201][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.fleet-fileds-fromhost-meta] for index patterns [.fleet-fileds-fromhost-meta-*]
[2025-10-06T03:50:26,211][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.fleet-fileds-tohost-data] for index patterns [.fleet-fileds-tohost-data-*]
[2025-10-06T03:50:26,218][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.fleet-fileds-fromhost-data] for index patterns [.fleet-fileds-fromhost-data-*]
[2025-10-06T03:50:26,225][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.fleet-fileds-tohost-meta] for index patterns [.fleet-fileds-tohost-meta-*]
[2025-10-06T03:50:26,228][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [.deprecation-indexing-settings]
[2025-10-06T03:50:26,234][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [apm-10d@lifecycle]
[2025-10-06T03:50:26,237][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_summary.1m-fallback@ilm]
[2025-10-06T03:50:26,240][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces-apm.sampled-fallback@ilm]
[2025-10-06T03:50:26,252][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_destination@mappings]
[2025-10-06T03:50:26,258][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.transaction@mappings]
[2025-10-06T03:50:26,262][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [apm-390d@lifecycle]
[2025-10-06T03:50:26,265][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.transaction.1m-fallback@ilm]
[2025-10-06T03:50:26,268][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [apm-90d@lifecycle]
[2025-10-06T03:50:26,270][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces-apm.rum-fallback@ilm]
[2025-10-06T03:50:26,273][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [apm@settings]
[2025-10-06T03:50:26,278][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_destination.10m-fallback@ilm]
[2025-10-06T03:50:26,283][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_destination.60m-fallback@ilm]
[2025-10-06T03:50:26,288][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [apm-180d@lifecycle]
[2025-10-06T03:50:26,292][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [apm@mappings]
[2025-10-06T03:50:26,296][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces-apm.rum@mappings]
[2025-10-06T03:50:26,300][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs-apm.app-fallback@ilm]
[2025-10-06T03:50:26,302][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_transaction.10m-fallback@ilm]
[2025-10-06T03:50:26,304][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm@mappings]
[2025-10-06T03:50:26,306][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.app-fallback@ilm]
[2025-10-06T03:50:26,309][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.transaction.10m-fallback@ilm]
[2025-10-06T03:50:26,312][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces-apm-fallback@ilm]
[2025-10-06T03:50:26,316][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [traces-apm@mappings]
[2025-10-06T03:50:26,318][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_summary.10m-fallback@ilm]
[2025-10-06T03:50:26,319][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_transaction.60m-fallback@ilm]
[2025-10-06T03:50:26,320][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_destination.1m-fallback@ilm]
[2025-10-06T03:50:26,325][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_transaction@mappings]
[2025-10-06T03:50:26,329][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_summary.60m-fallback@ilm]
[2025-10-06T03:50:26,332][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.internal-fallback@ilm]
[2025-10-06T03:50:26,335][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_transaction.1m-fallback@ilm]
[2025-10-06T03:50:26,337][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs-apm.error-fallback@ilm]
[2025-10-06T03:50:26,338][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.transaction.60m-fallback@ilm]
[2025-10-06T03:50:26,386][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs-apm.error@mappings]
[2025-10-06T03:50:26,389][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs-apm@settings]
[2025-10-06T03:50:26,392][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm.service_summary@mappings]
[2025-10-06T03:50:26,394][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [metrics-apm@settings]
[2025-10-06T03:50:26,751][INFO ][o.e.c.m.MetadataCreateIndexService] [ZSS] creating index [.security-7] in project [default], cause [api], templates [], shards [1]/[1]
[2025-10-06T03:50:26,775][INFO ][o.e.c.r.a.AllocationService] [ZSS] in project [default] updating number_of_replicas to [0] for indices [.security-7]
[2025-10-06T03:50:26,783][INFO ][o.e.x.w.LicensedWriteLoadForecaster] [ZSS] license state changed, now [valid]
[2025-10-06T03:50:27,124][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [elastic-connectors] for index patterns [.elastic-connectors-v1]
[2025-10-06T03:50:27,134][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [elastic-connectors-sync-jobs] for index patterns [.elastic-connectors-sync-jobs-v1]
[2025-10-06T03:50:27,174][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-otel@template] for index patterns [metrics-*.otel-*]
[2025-10-06T03:50:27,188][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_destination.1m@template] for index patterns [metrics-service_destination.1m.otel-*]
[2025-10-06T03:50:27,207][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_summary.60m.otel@template] for index patterns [metrics-service_summary.60m.otel-*]
[2025-10-06T03:50:27,222][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [traces-otel@template] for index patterns [traces-*.otel-*]
[2025-10-06T03:50:27,238][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-transaction.60m.otel@template] for index patterns [metrics-transaction.60m.otel-*]
[2025-10-06T03:50:27,260][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-transaction.1m.otel@template] for index patterns [metrics-transaction.1m.otel-*]
[2025-10-06T03:50:27,280][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_destination.60m@template] for index patterns [metrics-service_destination.60m.otel-*]
[2025-10-06T03:50:27,299][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_transaction.1m.otel@template] for index patterns [metrics-service_transaction.1m.otel-*]
[2025-10-06T03:50:27,317][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_transaction.10m.otel@template] for index patterns [metrics-service_transaction.10m.otel-*]
[2025-10-06T03:50:27,336][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-transaction.10m.otel@template] for index patterns [metrics-transaction.10m.otel-*]
[2025-10-06T03:50:27,353][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_summary.1m.otel@template] for index patterns [metrics-service_summary.1m.otel-*]
[2025-10-06T03:50:27,372][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_transaction.60m.otel@template] for index patterns [metrics-service_transaction.60m.otel-*]
[2025-10-06T03:50:27,377][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [agentless] for index patterns [agentless-*-*]
[2025-10-06T03:50:27,384][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics] for index patterns [metrics-*-*]
[2025-10-06T03:50:27,399][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_summary.10m.otel@template] for index patterns [metrics-service_summary.10m.otel-*]
[2025-10-06T03:50:27,404][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [synthetics] for index patterns [synthetics-*-*]
[2025-10-06T03:50:27,421][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.transaction.10m@template] for index patterns [metrics-apm.transaction.10m-*]
[2025-10-06T03:50:27,566][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.kibana-reporting] for index patterns [.kibana-reporting*]
[2025-10-06T03:50:27,577][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [logs-apm.error@template] for index patterns [logs-apm.error-*]
[2025-10-06T03:50:27,599][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-service_destination.10m@template] for index patterns [metrics-service_destination.10m.otel-*]
[2025-10-06T03:50:27,604][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.deprecation-indexing-template-9] for index patterns [.logs-elasticsearch.deprecation-*]
[2025-10-06T03:50:27,616][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.internal@template] for index patterns [metrics-apm.internal-*]
[2025-10-06T03:50:27,627][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_summary.10m@template] for index patterns [metrics-apm.service_summary.10m-*]
[2025-10-06T03:50:27,632][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [.deprecation-indexing-template] for index patterns [.logs-deprecation.*]
[2025-10-06T03:50:27,642][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_transaction.60m@template] for index patterns [metrics-apm.service_transaction.60m-*]
[2025-10-06T03:50:27,650][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_destination.60m@template] for index patterns [metrics-apm.service_destination.60m-*]
[2025-10-06T03:50:27,662][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_transaction.10m@template] for index patterns [metrics-apm.service_transaction.10m-*]
[2025-10-06T03:50:27,674][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_destination.10m@template] for index patterns [metrics-apm.service_destination.10m-*]
[2025-10-06T03:50:27,684][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_summary.60m@template] for index patterns [metrics-apm.service_summary.60m-*]
[2025-10-06T03:50:27,693][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.app@template] for index patterns [metrics-apm.app.*-*]
[2025-10-06T03:50:27,703][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_destination.1m@template] for index patterns [metrics-apm.service_destination.1m-*]
[2025-10-06T03:50:27,713][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.transaction.60m@template] for index patterns [metrics-apm.transaction.60m-*]
[2025-10-06T03:50:27,721][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_transaction.1m@template] for index patterns [metrics-apm.service_transaction.1m-*]
[2025-10-06T03:50:27,735][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.service_summary.1m@template] for index patterns [metrics-apm.service_summary.1m-*]
[2025-10-06T03:50:27,743][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [metrics-apm.transaction.1m@template] for index patterns [metrics-apm.transaction.1m-*]
[2025-10-06T03:50:27,752][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [traces-apm.rum@template] for index patterns [traces-apm.rum-*]
[2025-10-06T03:50:27,760][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [logs-apm.app@template] for index patterns [logs-apm.app.*-*]
[2025-10-06T03:50:27,768][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [traces-apm@template] for index patterns [traces-apm-*]
[2025-10-06T03:50:27,790][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [traces-apm.sampled@template] for index patterns [traces-apm.sampled-*]
[2025-10-06T03:50:28,385][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [.monitoring-8-ilm-policy]
[2025-10-06T03:50:28,386][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [ml-size-based-ilm-policy]
[2025-10-06T03:50:28,387][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics]
[2025-10-06T03:50:28,388][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [logs]
[2025-10-06T03:50:28,389][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [synthetics]
[2025-10-06T03:50:28,390][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [7-days-default]
[2025-10-06T03:50:28,390][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [90-days-default]
[2025-10-06T03:50:28,393][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [30-days-default]
[2025-10-06T03:50:28,393][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [180-days-default]
[2025-10-06T03:50:28,394][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [365-days-default]
[2025-10-06T03:50:28,395][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [synthetics@lifecycle]
[2025-10-06T03:50:28,396][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics@lifecycle]
[2025-10-06T03:50:28,397][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [logs@lifecycle]
[2025-10-06T03:50:28,398][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [traces@lifecycle]
[2025-10-06T03:50:28,399][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [90-days@lifecycle]
[2025-10-06T03:50:28,400][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [7-days@lifecycle]
[2025-10-06T03:50:28,402][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [30-days@lifecycle]
[2025-10-06T03:50:28,403][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [180-days@lifecycle]
[2025-10-06T03:50:28,404][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [365-days@lifecycle]
[2025-10-06T03:50:28,405][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [watch-history-ilm-policy-16]
[2025-10-06T03:50:28,410][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [slm-history-ilm-policy]
[2025-10-06T03:50:28,410][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [ilm-history-ilm-policy]
[2025-10-06T03:50:28,411][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [.deprecation-indexing-ilm-policy]
[2025-10-06T03:50:28,411][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [.fleet-actions-results-ilm-policy]
[2025-10-06T03:50:28,412][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [.fleet-file-tohost-data-ilm-policy]
[2025-10-06T03:50:28,413][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [.fleet-file-tohost-meta-ilm-policy]
[2025-10-06T03:50:28,414][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [.fleet-file-fromhost-data-ilm-policy]
[2025-10-06T03:50:28,415][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [.fleet-file-fromhost-meta-ilm-policy]
[2025-10-06T03:50:28,416][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_destination_60m_metrics-default_policy]
[2025-10-06T03:50:28,417][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [logs-apm.app_logs-default_policy]
[2025-10-06T03:50:28,418][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_summary_10m_metrics-default_policy]
[2025-10-06T03:50:28,418][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [logs-apm.error_logs-default_policy]
[2025-10-06T03:50:28,419][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.internal_metrics-default_policy]
[2025-10-06T03:50:28,420][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_destination_10m_metrics-default_policy]
[2025-10-06T03:50:28,421][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_transaction_10m_metrics-default_policy]
[2025-10-06T03:50:28,428][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_transaction_1m_metrics-default_policy]
[2025-10-06T03:50:28,429][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_summary_1m_metrics-default_policy]
[2025-10-06T03:50:28,429][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.app_metrics-default_policy]
[2025-10-06T03:50:28,430][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_destination_1m_metrics-default_policy]
[2025-10-06T03:50:28,430][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_summary_60m_metrics-default_policy]
[2025-10-06T03:50:28,431][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.transaction_1m_metrics-default_policy]
[2025-10-06T03:50:28,432][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.transaction_10m_metrics-default_policy]
[2025-10-06T03:50:28,433][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.transaction_60m_metrics-default_policy]
[2025-10-06T03:50:28,433][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [traces-apm.sampled_traces-default_policy]
[2025-10-06T03:50:28,434][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [traces-apm.rum_traces-default_policy]
[2025-10-06T03:50:28,435][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [traces-apm.traces-default_policy]
[2025-10-06T03:50:28,436][INFO ][o.e.x.i.a.TransportPutLifecycleAction] [ZSS] adding index lifecycle policy [metrics-apm.service_transaction_60m_metrics-default_policy]
[2025-10-06T03:50:28,776][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline behavioral_analytics-events-final_pipeline
[2025-10-06T03:50:28,777][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline reindex-data-stream-pipeline
[2025-10-06T03:50:28,778][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline logs-default-pipeline
[2025-10-06T03:50:28,779][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline logs@default-pipeline
[2025-10-06T03:50:28,782][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline logs-apm.error@default-pipeline
[2025-10-06T03:50:28,782][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline metrics-apm.service_destination@default-pipeline
[2025-10-06T03:50:28,783][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline logs-apm.app@default-pipeline
[2025-10-06T03:50:28,783][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline traces-apm@default-pipeline
[2025-10-06T03:50:28,784][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline traces-apm.rum@default-pipeline
[2025-10-06T03:50:28,785][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline metrics-apm.transaction@default-pipeline
[2025-10-06T03:50:28,785][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline metrics-apm.app@default-pipeline
[2025-10-06T03:50:28,786][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline metrics-apm.service_transaction@default-pipeline
[2025-10-06T03:50:28,786][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline metrics-apm.service_summary@default-pipeline
[2025-10-06T03:50:28,786][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline apm@pipeline
[2025-10-06T03:50:28,787][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline search-default-ingestion
[2025-10-06T03:50:28,788][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline logs@json-message
[2025-10-06T03:50:28,791][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline logs@json-pipeline
[2025-10-06T03:50:28,800][INFO ][o.e.c.r.a.AllocationService] [ZSS] current.health="GREEN" message="Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[.security-7][0]]])." previous.health="YELLOW" reason="shards started [[.security-7][0]]"
[2025-10-06T03:50:28,911][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs-settings]
[2025-10-06T03:50:28,913][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [logs@settings]
[2025-10-06T03:50:28,915][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding component template [behavioral_analytics-events-settings]
[2025-10-06T03:50:29,040][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [behavioral_analytics-events-default] for index patterns [behavioral_analytics-events-*]
[2025-10-06T03:50:29,050][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [logs] for index patterns [logs-*-*]
[2025-10-06T03:50:29,064][INFO ][o.e.c.m.MetadataIndexTemplateService] [ZSS] adding index template [logs-otel@template] for index patterns [logs-*.otel-*]
[2025-10-06T03:50:29,388][INFO ][o.e.h.n.s.HealthNodeTaskExecutor] [ZSS] Node [{ZSS}{flAjod6OSo29EiZMhLt6zQ}] is selected as the current health node.
[2025-10-06T03:50:29,601][INFO ][o.e.x.s.a.Realms         ] [ZSS] license mode is [basic], currently licensed security realms are [reserved/reserved,file/default_file,native/default_native]
[2025-10-06T03:50:29,608][INFO ][o.e.l.ClusterStateLicenseService] [ZSS] license [4965f85f-6646-4d8a-bb80-eaf0ae1686a2] mode [basic] - valid
[2025-10-06T03:50:29,887][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline logs-apm@pipeline
[2025-10-06T03:50:29,887][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline metrics-apm.internal@default-pipeline
[2025-10-06T03:50:29,888][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline metrics-apm@pipeline
[2025-10-06T03:50:29,888][INFO ][o.e.x.c.t.IndexTemplateRegistry] [ZSS] adding ingest pipeline traces-apm@pipeline
[2025-10-06T03:50:29,889][INFO ][o.e.x.w.LicensedWriteLoadForecaster] [ZSS] license state changed, now [not valid]
[2025-10-06T03:50:29,992][INFO ][o.e.x.s.s.QueryableBuiltInRolesSynchronizer] [ZSS] Successfully synced [29] built-in roles to .security index
[2025-10-06T03:50:30,062][INFO ][o.e.x.s.s.SecurityMigrationExecutor] [ZSS] Security migration not needed. Setting current version to: [2]
[2025-10-06T03:50:30,552][INFO ][o.e.c.m.MetadataCreateIndexService] [ZSS] creating index [.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001] in project [default], cause [initialize_data_stream], templates [provided in request], shards [1]/[1]
[2025-10-06T03:50:30,556][INFO ][o.e.c.m.MetadataCreateDataStreamService] [ZSS] adding data stream [.logs-elasticsearch.deprecation-default] with write index [.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001], backing indices [], and aliases []
[2025-10-06T03:50:30,559][INFO ][o.e.c.r.a.AllocationService] [ZSS] in project [default] updating number_of_replicas to [0] for indices [.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001]
[2025-10-06T03:50:31,150][INFO ][o.e.x.i.IndexLifecycleTransition] [ZSS] moving index [.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001] from [null] to [{"phase":"new","action":"complete","name":"complete"}] in policy [.deprecation-indexing-ilm-policy]
[2025-10-06T03:50:31,292][INFO ][o.e.c.r.a.AllocationService] [ZSS] current.health="GREEN" message="Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001][0]]])." previous.health="YELLOW" reason="shards started [[.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001][0]]"
[2025-10-06T03:50:31,382][INFO ][o.e.x.i.IndexLifecycleTransition] [ZSS] moving index [.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001] from [{"phase":"new","action":"complete","name":"complete"}] to [{"phase":"hot","action":"unfollow","name":"branch-check-unfollow-prerequisites"}] in policy [.deprecation-indexing-ilm-policy]
[2025-10-06T03:50:31,473][INFO ][o.e.c.m.MetadataMappingService] [ZSS] [.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001/iXOKRefVTVC_b9Bh9_Uz2g] update_mapping [_doc]
[2025-10-06T03:50:31,575][INFO ][o.e.x.i.IndexLifecycleTransition] [ZSS] moving index [.ds-.logs-elasticsearch.deprecation-default-2025.10.05-000001] from [{"phase":"hot","action":"unfollow","name":"branch-check-unfollow-prerequisites"}] to [{"phase":"hot","action":"rollover","name":"check-rollover-ready"}] in policy [.deprecation-indexing-ilm-policy]
[2025-10-06T03:50:34,194][INFO ][o.e.x.s.InitialNodeSecurityAutoConfiguration] [ZSS] HTTPS has been configured with automatically generated certificates, and the CA's hex-encoded SHA-256 fingerprint is [48f63aa53916564527b99e3586eee4c25d22cfdffd46c5b9d4e41fd8c6abb9f4]
[2025-10-06T03:50:34,206][INFO ][o.e.x.s.e.InternalEnrollmentTokenGenerator] [ZSS] Will not generate node enrollment token because node is only bound on localhost for transport and cannot connect to nodes from other hosts




鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣
鉁?Elasticsearch security features have been automatically configured!
鉁?Authentication is enabled and cluster connections are encrypted.

鈩癸笍  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  ikQsJT6DFOZQX_6b-wl0

鈩癸笍  HTTP CA certificate SHA-256 fingerprint:
  48f63aa53916564527b99e3586eee4c25d22cfdffd46c5b9d4e41fd8c6abb9f4

鈩癸笍  Configure Kibana to use this cluster:
鈥?Run Kibana and click the configuration link in the terminal when Kibana starts.
鈥?Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjE0LjAiLCJhZHIiOlsiMTkyLjE2OC4zMS41ODo5MjAwIl0sImZnciI6IjQ4ZjYzYWE1MzkxNjU2NDUyN2I5OWUzNTg2ZWVlNGMyNWQyMmNmZGZmZDQ2YzViOWQ0ZTQxZmQ4YzZhYmI5ZjQiLCJrZXkiOiJJWUh0dFprQm5fVkVQbFBsQjFqdjpKR0cxd3lJYkVzbzhhN3Q2T2ZremZ3In0=

鈩癸笍  Configure other nodes to join this cluster:
鈥?On this node:
  鈦?Create an enrollment token with `bin/elasticsearch-create-enrollment-token -s node`.
  鈦?Uncomment the transport.host setting at the end of config/elasticsearch.yml.
  鈦?Restart Elasticsearch.
鈥?On other nodes:
  鈦?Start Elasticsearch with `bin/elasticsearch --enrollment-token <token>`, using the enrollment token that you generated.
鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣鈹佲攣



攣




[2025-10-06T03:50:36,300][INFO ][o.e.c.m.MetadataCreateIndexService] [ZSS] creating index [.ds-ilm-history-7-2025.10.05-000001] in project [default], cause [initialize_data_stream], templates [provided in request], shards [1]/[1]
[2025-10-06T03:50:36,301][INFO ][o.e.c.m.MetadataCreateDataStreamService] [ZSS] adding data stream [ilm-history-7] with write index [.ds-ilm-history-7-2025.10.05-000001], backing indices [], and aliases []
[2025-10-06T03:50:36,302][INFO ][o.e.c.r.a.AllocationService] [ZSS] in project [default] updating number_of_replicas to [0] for indices [.ds-ilm-history-7-2025.10.05-000001]
[2025-10-06T03:50:36,683][INFO ][o.e.c.r.a.AllocationService] [ZSS] current.health="GREEN" message="Cluster health status changed from [YELLOW] to [GREEN] (reason: [shards started [[.ds-ilm-history-7-2025.10.05-000001][0]]])." previous.health="YELLOW" reason="shards started [[.ds-ilm-history-7-2025.10.05-000001][0]]"
