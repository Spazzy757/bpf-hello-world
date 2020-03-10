#!/usr/bin/python
from bcc import BPF
print("tracing sys_sync()")
BPF(
    text='int kprobe__sys_sync(void *ctx) { bpf_trace_printk("sys_sync() called\\n"); return 0;}'
).trace_print()
