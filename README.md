# MXNet Profiler Demo
Collection of example usecases to show how to use Apache MXNet Profiler.

# Usecases
1. I want to just view summary (Time and Memory usage) of my run. How to do that?
2. Which operators in my Network takes maximum time?
3. What is the Average and Max memory usage across different devices (CPU, GPU/0, GPU/1..)
4. Which operator ran on which GPUs? Timeline, Markers and Ranges?
5. How to identify performance bottleneck due to data transfer between CPU/GPU?
6. How can I view more detailed profiler output like what GPU kernels were called, how much time it took? How to use NVProf with MXNet profiler?

# Known Issues and Missing Functionalities
1. Cannot view the Chrome tracing with continuous dump i.e., cannot use in real time for long running jobs.

Even though MXNet supports continuous period dump of profile output, it cannot be viewed in real time as the file content will be of invalid syntax to open in Chrome Tracing.

2. MXNet Profiler do not show Avg and Max device utilization i.e., CPU/GPU utilization

3. There is no aggregation functionality to easily view operator taking max time, identify bottlenecks like CPU/GPU data transfer taking more time. Users need to parse chrome tracing output JSOn file or profiler dumps console output.

4. There is no anamoly detection. Example: If a RNN operator takes 10x more time every few epochs, then, there is no easy way to understand it.

5. Operators do not show what was the input. This makes it hard to build a depedency graph and apply time stamps on top of it.

# References
1. MXNet Profiler API - http://mxnet.incubator.apache.org/api/python/profiler/profiler.html?highlight=profile#module-mxnet.profiler
2. MXNet Profiler Tutorials - http://mxnet.incubator.apache.org/versions/master/tutorials/python/profiler.html
3. MXNet Documentation - http://mxnet.incubator.apache.org/
