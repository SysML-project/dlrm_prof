import os

os.environ['NCCL_ALGO'] = 'Ring'
os.environ['NCCL_DEBUG'] = 'INFO'
os.environ['NCCL_DEBUG_FILE'] = 'debug.%h.%p'
os.environ['NCCL_DEBUG_SUBSYS'] = 'ALL'
os.environ['NCCL_TOPO_DUMP_FILE'] = 'topo.xml'
os.environ['TORCH_DISTRIBUTED_DEBUG'] = 'INFO'
os.environ['NCCL_COLLNET_ENABLE'] = '0'
os.environ['NCCL_DMABUF_ENABLE'] = '1'

