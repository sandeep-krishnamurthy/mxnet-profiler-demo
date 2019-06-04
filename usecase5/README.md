# Profiler Console Summary Output

```
Profile Statistics.
        Note that counter items are counter values and not time units.
Device Storage
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
Memory: gpu/0                           4      400000.0000           0.0000      800000.0000      400000.0000
Memory: cpu/0                           1      400000.0000      400000.0000      400000.0000           0.0000

MXNET_C_API
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
MXNDArrayFree                           2           0.0010           0.0000           0.0010           0.0005
MXNDArrayGetDType                       2           0.0010           0.0000           0.0010           0.0005
MXNet C API Calls                      15           0.0150           0.0010           0.0150           0.0070
MXImperativeInvokeEx                    3        1588.3420           0.0460        1588.2430         529.4473
MXNDArrayGetShape                       2           0.0030           0.0010           0.0020           0.0015
MXNet C API Concurrency                30           0.0000           0.0000           0.0010           0.0005
MXNDArrayWaitAll                        1         134.1310         134.1310         134.1310         134.1310
MXNDArrayCreateEx                       2           0.0110           0.0050           0.0060           0.0055
MXNDArrayGetContext                     3           0.0020           0.0000           0.0010           0.0007

operator
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
DeleteVariable                          4           1.9920           0.0080           0.9890           0.4980
CopyCPU2GPU                             4         430.3880          80.9720         134.2240         107.5970
broadcast_add                           2          86.4500          43.2220          43.2280          43.2250
```

