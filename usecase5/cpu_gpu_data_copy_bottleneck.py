import mxnet as mx
from mxnet import nd
from mxnet import profiler

profiler.set_config(profile_all=True, aggregate_stats=True, filename='cpu_gpu_data_copy_profiler_output.json')

# Create a large Tensor on CPU
data1 = nd.random.uniform(shape=(10000, 10000), ctx=mx.cpu())
data2 = nd.random.uniform(shape=(10000, 10000), ctx=mx.cpu())
nd.waitall()

# Profiler copying data and operation only

profiler.set_state('run')

# Copy data to GPU
data1.as_in_context(context= mx.gpu(0))
data2.as_in_context(context= mx.gpu(0))

# Do couple of operations on GPU
res = data1 + data2
#res = nd.mean(res)
# Copy result back to CPU
res_cpu = res.as_in_context(context=mx.cpu())
nd.waitall()
profiler.set_state('stop')
print(profiler.dumps())

profiler.dump()

