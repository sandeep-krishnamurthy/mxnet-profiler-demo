# CPU output

Profile Statistics.
        Note that counter items are counter values and not time units.
Device Storage
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
Memory: cpu/0                         264        2948.8799           0.2560       14080.7842        7040.2642

MXNET_C_API
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
MXNDArrayWaitAll                        1          51.0570          51.0570          51.0570          51.0570
MXNDArrayGetGradState                   8           0.0110           0.0010           0.0020           0.0014
MXNDArrayGetStorageType                16           0.0250           0.0010           0.0030           0.0016
MXAutogradBackwardEx                    1           0.8700           0.8700           0.8700           0.8700
MXNDArraySetGradState                   8           0.0100           0.0010           0.0020           0.0012
MXAutogradSetIsTraining                 2           0.0030           0.0010           0.0020           0.0015
MXNDArrayGetContext                    78           0.0780           0.0000           0.0020           0.0010
MXNDArrayCreateEx                       1           0.0160           0.0160           0.0160           0.0160
MXNDArrayGetShape                      67           0.0690           0.0000           0.0080           0.0010
MXImperativeInvokeEx                   81           2.0730           0.0090           0.2320           0.0256
MXAutogradSetIsRecording                2           0.0020           0.0010           0.0010           0.0010
MXNet C API Concurrency               978           0.0000           0.0000           0.0010           0.0005
MXNDArrayAt                            64           0.1410           0.0010           0.0030           0.0022
MXNet C API Calls                     489           0.4890           0.0010           0.4890           0.2440
MXNDArrayGetDType                      17           0.0190           0.0000           0.0020           0.0011
MXNDArrayFree                         142           0.9400           0.0000           0.0360           0.0066
MXNDArraySyncCopyFromCPU                1           5.9240           5.9240           5.9240           5.9240

operator
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
_backward_Pooling                       4           2.0100           0.2730           0.7330           0.5025
_backward_copy                          2           0.1190           0.0580           0.0610           0.0595
_backward_pick                          2           0.0690           0.0330           0.0360           0.0345
_zeros_without_dtype                    4           0.3410           0.0460           0.1250           0.0852
_backward_mul_scalar                    2           0.0310           0.0140           0.0170           0.0155
SetValueOp                              2           0.0260           0.0120           0.0140           0.0130
pick                                    2           0.0350           0.0160           0.0190           0.0175
DeleteVariable                        270          34.8840           0.0020           8.2660           0.1292
_image_to_tensor                      128           1.7220           0.0090           0.0260           0.0135
Pooling                                 4           4.7740           0.5860           1.8010           1.1935
Convolution                             4           5.4090           1.0310           1.6730           1.3522
WaitForVar                              2           0.0200           0.0090           0.0110           0.0100
_backward_mean                          2           0.1090           0.0530           0.0560           0.0545
_backward_FullyConnected                4           1.0930           0.0510           0.4950           0.2733
Activation                              6           0.9550           0.0380           0.3820           0.1592
stack                                   2           0.9000           0.4480           0.4520           0.4500
Flatten                                 2           0.1200           0.0580           0.0620           0.0600
FullyConnected                          4           0.7230           0.0680           0.2940           0.1807
log_softmax                             2           0.0480           0.0220           0.0260           0.0240
_backward_Convolution                   4           9.2630           1.0300           3.6010           2.3157
_mul_scalar                             2           0.0180           0.0080           0.0100           0.0090
_backward_log_softmax                   2           0.0370           0.0170           0.0200           0.0185
mean                                    2           0.0620           0.0300           0.0320           0.0310
_backward_Activation                    6           1.3600           0.0460           0.5740           0.2267
multi_sgd_update                        4           1.3740           0.0640           0.6230           0.3435


------------------------------------------------------------------------

# GPU output

Profile Statistics.
        Note that counter items are counter values and not time units.
Device Storage
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
Memory: cpu/0                         130         200.9600           3.1360         401.6640         199.2640
Memory: gpu/0                         147         200.7040         200.7040       25221.8926       12510.5938

MXNET_C_API
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
MXNDArrayWaitAll                        1          80.3030          80.3030          80.3030          80.3030
MXNDArrayGetGradState                   8           0.0070           0.0000           0.0020           0.0009
MXNDArrayGetStorageType                16           0.0130           0.0000           0.0010           0.0008
MXAutogradBackwardEx                    1           0.5490           0.5490           0.5490           0.5490
MXNDArraySetGradState                   8           0.0070           0.0000           0.0010           0.0009
MXAutogradSetIsTraining                 2           0.0020           0.0010           0.0010           0.0010
MXNDArrayGetContext                    78           0.0700           0.0000           0.0020           0.0009
MXNDArrayCreateEx                       3           0.0100           0.0020           0.0050           0.0033
MXNDArrayGetShape                      69           0.0720           0.0000           0.0020           0.0010
MXImperativeInvokeEx                   83           2.0030           0.0120           0.0760           0.0241
MXAutogradSetIsRecording                2           0.0020           0.0000           0.0020           0.0010
MXNet C API Concurrency               998           0.0000           0.0000           0.0010           0.0005
MXNDArrayAt                            64           0.1310           0.0010           0.0030           0.0020
MXNet C API Calls                     499           0.4990           0.0010           0.4990           0.2490
MXNDArrayGetDType                      19           0.0170           0.0000           0.0010           0.0009
MXNDArrayFree                         144           0.6390           0.0000           0.0170           0.0044
MXNDArraySyncCopyFromCPU                1           0.3530           0.3530           0.3530           0.3530

operator
=================
Name                          Total Count        Time (ms)    Min Time (ms)    Max Time (ms)    Avg Time (ms)
----                          -----------        ---------    -------------    -------------    -------------
CopyCPU2GPU                             4          93.3890          23.3380          23.3560          23.3472
_backward_copy                          2           0.1800           0.0890           0.0910           0.0900
SetValueOp                              2          43.8330          21.9150          21.9180          21.9165
pick                                    2           0.0660           0.0320           0.0340           0.0330
_backward_pick                          2           0.1110           0.0540           0.0570           0.0555
_zeros_without_dtype                    4           2.1330           0.4470           0.6200           0.5332
_backward_mul_scalar                    2           0.0980           0.0480           0.0500           0.0490
_image_to_tensor                      128           2.0670           0.0060           0.1970           0.0161
Pooling                                 4           0.2710           0.0490           0.0860           0.0677
DeleteVariable                        268           4.6220           0.0010           1.0980           0.0172
_backward_FullyConnected                4           0.7320           0.0960           0.2700           0.1830
_backward_mean                          2           1.7380           0.8680           0.8700           0.8690
_backward_Pooling                       4           0.5480           0.1240           0.1500           0.1370
Convolution                             4           1.4200           0.2580           0.4520           0.3550
WaitForVar                              2           0.0190           0.0090           0.0100           0.0095
Activation                              6           0.2830           0.0290           0.0730           0.0472
stack                                   2           0.8610           0.4290           0.4320           0.4305
Flatten                                 2           0.0630           0.0310           0.0320           0.0315
FullyConnected                          4           0.6900           0.1410           0.2040           0.1725
_backward_Convolution                   4           2.8870           0.6030           0.8400           0.7218
_mul_scalar                             2           0.0550           0.0260           0.0290           0.0275
_backward_Activation                    6           0.4010           0.0380           0.1060           0.0668
log_softmax                             2           0.0770           0.0370           0.0400           0.0385
multi_sgd_update                        4           0.2890           0.0450           0.0990           0.0723
mean                                    2           0.0750           0.0360           0.0390           0.0375
_backward_log_softmax                   2           0.1140           0.0560           0.0580           0.0570

