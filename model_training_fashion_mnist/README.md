# CPU Console Output

```
Profile Statistics.
        Note that counter items are counter values and not time units.
Device Storage
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
Memory: cpu/0                       15015       60979.7266           0.6000       65137.4258       32568.4121
Memory: cpu shared/                   878       24416.6406         802.8160       26525.6953       12861.4404

MXNET_C_API
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
MXNDArrayGetGradState                2350           2.2410           0.0000           0.0070           0.0010
MXNDArrayGetStorageType              4700           4.1650           0.0000           0.0470           0.0009
MXAutogradBackwardEx                  235         270.1940           0.5800           2.8100           1.1498
MXNDArrayFree                        4231           5.2580           0.0000           0.0550           0.0012
MXAutogradMarkVariables                 5           0.0590           0.0050           0.0370           0.0118
MXNDArrayCreateEx                       5           0.0100           0.0020           0.0020           0.0020
MXNDArrayGetDType                    4720           3.8360           0.0000           0.0540           0.0008
MXImperativeInvokeEx                 4485         307.6870           0.0140           8.1200           0.0686
MXNDArrayCreateFromSharedMem             470          14.8800           0.0090           0.7480           0.0317
MXNDArraySetGradState                2350           2.1520           0.0000           0.0470           0.0009
MXAutogradSetIsTraining               480           0.4610           0.0000           0.0310           0.0010
MXNDArrayGetContext                  3060           2.8810           0.0000           0.0460           0.0009
MXSymbolSetAttr                        55           0.0910           0.0000           0.0040           0.0017
MXAutogradSetIsRecording              480           0.4820           0.0000           0.0050           0.0010
MXNet C API Concurrency             55320           0.0000           0.0000           0.0010           0.0005
MXNet C API Calls                   27660          27.6600           0.0010          27.6600          13.8295
MXSymbolCreateAtomicSymbol               9           0.2520           0.0080           0.0970           0.0280
MXNDArrayGetShape                      20           0.0160           0.0000           0.0010           0.0008
MXSymbolInferShape                      5           0.3250           0.0390           0.1060           0.0650

operator
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
_backward_Pooling                     816         382.2670           0.2470           6.0930           0.4685
_backward_copy                        408          33.9740           0.0550           0.3640           0.0833
_backward_Activation                 1632         297.8970           0.0270           1.3540           0.1825
SetValueOp                            470           7.1540           0.0080           0.0550           0.0152
_zeros                                 20           0.8960           0.0070           0.1370           0.0448
Convolution                           820         723.4870           0.3130          13.7670           0.8823
_zeros_without_dtype                  940          21.5570           0.0110           0.2170           0.0229
_backward_pick                        470          15.1810           0.0210           0.2440           0.0323
DeleteVariable                      16112         246.5470           0.0000           0.5780           0.0153
ResourceParallelRandomSetSeed               2          10.1270           5.0620           5.0650           5.0635
_backward_Convolution                 816        1148.4480           0.9510           1.9200           1.4074
_mul_scalar                           408           3.7430           0.0050           0.0400           0.0092
pick                                  408           7.4120           0.0110           0.0730           0.0182
_random_uniform                        10          55.2400           0.0120          27.3340           5.5240
Pooling                               818         574.7270           0.2000           1.4120           0.7026
_backward_mul_scalar                  470           4.7380           0.0050           0.0240           0.0101
Activation                           1636         112.4120           0.0180           0.8040           0.0687
Flatten                               408         138.7550           0.2320           1.1150           0.3401
FullyConnected                       1224         112.6100           0.0360           0.9580           0.0920
CopyCPU2CPU                            10           0.3660           0.0070           0.1380           0.0366
log_softmax                           408          10.5920           0.0190           0.0730           0.0260
mean                                  408          11.3520           0.0160           0.4600           0.0278
_backward_log_softmax                 408           8.7480           0.0160           0.0650           0.0214
_backward_mean                        470          13.5120           0.0150           0.3230           0.0287
_backward_FullyConnected             1224         137.2730           0.0380           2.0390           0.1122
multi_sgd_update                     1224          46.3580           0.0080           0.2660           0.0379

```

# GPU Output

```

Profile Statistics.
        Note that counter items are counter values and not time units.
Device Storage
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
Memory: cpu shared/                   940         301.4400           0.0000        4018.1760        2009.0880
Memory: cpu/0                          14           0.0320           0.0320         232.3440         116.1560
Memory: gpu/0                       18288       25062.0039         802.8160       61099.2539       30148.2188

MXNET_C_API
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
MXNDArrayGetGradState                2350           1.4690           0.0000           0.0250           0.0006
MXNDArrayGetStorageType              4700           2.5040           0.0000           0.0020           0.0005
MXAutogradBackwardEx                  235         180.9500           0.6080           2.3870           0.7700
MXAutogradMarkVariables                 5           0.0390           0.0070           0.0080           0.0078
MXSymbolInferShape                      5           0.2360           0.0410           0.0560           0.0472
MXSymbolSetAttr                        55           0.1650           0.0010           0.0160           0.0030
MXNDArraySetGradState                2350           1.3110           0.0000           0.0230           0.0006
MXAutogradSetIsTraining               480           0.2770           0.0000           0.0020           0.0006
MXNDArrayGetContext                  3530           2.1330           0.0000           0.0040           0.0006
MXNDArrayCreateEx                     475           1.1560           0.0010           0.0910           0.0024
MXNDArrayCreateFromSharedMem             470           5.5220           0.0080           0.0490           0.0117
MXNDArrayGetDType                    5190           2.6470           0.0000           0.0020           0.0005
MXNDArrayGetShape                     490           0.3100           0.0000           0.0020           0.0006
MXImperativeInvokeEx                 4955         245.1310           0.0120           0.3280           0.0495
MXNDArrayFree                        4701          13.6930           0.0000           0.1820           0.0029
MXSymbolCreateAtomicSymbol               9           0.2160           0.0140           0.0700           0.0240
MXNet C API Concurrency             60960           0.0000           0.0000           0.0010           0.0005
MXNet C API Calls                   30480          30.4800           0.0010          30.4800          15.2395
MXAutogradSetIsRecording              480           0.3080           0.0000           0.0140           0.0006

operator
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
CopyCPU2GPU                           950         534.8090           0.0310          48.5290           0.5630
_backward_copy                        468          18.5630           0.0290           0.0730           0.0397
SetValueOp                            470          33.5700           0.0160           1.6850           0.0714
_zeros                                 20         108.5910           0.0070          51.1340           5.4296
Flatten                               468          17.8830           0.0270           0.8500           0.0382
Activation                           1872          97.4180           0.0230           1.5580           0.0520
Pooling                               936          73.1950           0.0440           1.7680           0.0782
Convolution                           936         528.8530           0.1990          54.7670           0.5650
_zeros_without_dtype                  938          93.7440           0.0200           2.9110           0.0999
_backward_pick                        470          33.7670           0.0280           1.4020           0.0718
DeleteVariable                      19206         185.1810           0.0010           1.6690           0.0096
ResourceParallelRandomSetSeed               2          10.1180           5.0580           5.0600           5.0590
_backward_Pooling                     936         144.7210           0.1160           0.9310           0.1546
pick                                  468          15.2610           0.0210           0.0830           0.0326
_random_uniform                        10           4.5150           0.0120           2.0310           0.4515
_backward_mul_scalar                  470          25.3020           0.0180           1.9780           0.0538
FullyConnected                       1404         117.5150           0.0500           1.0300           0.0837
_backward_Convolution                 936         908.5480           0.5200           2.7570           0.9707
_mul_scalar                           468          12.4460           0.0180           0.0490           0.0266
_backward_log_softmax                 468          20.7760           0.0330           0.0840           0.0444
mean                                  468          19.4710           0.0300           0.1910           0.0416
multi_sgd_update                     1404          72.9120           0.0230           0.2070           0.0519
_backward_mean                        470         106.1990           0.0310          37.3540           0.2260
_backward_FullyConnected             1404         173.5300           0.0960           1.5530           0.1236
_backward_Activation                 1872         125.7280           0.0240           0.7410           0.0672
log_softmax                           468          23.0660           0.0390           0.3300           0.0493

```
