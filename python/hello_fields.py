from bcc import BPF

#define BPF program
prog = """
into hello(void *ctx) {
    bpf_trace_printk("Hello, World\\n");
    return 0;
}
"""

# Load BPF program
b = BPF(text=prog)
b.attach_kprobe(
    event=b.get_syscall_fnname("clone")
    fn_name="hello"
)

#header
print("%-18s %-16s %-6s %s" % ("TIME(s)", "COMM", "PID", "MESSAGE"))

# format output

while 1:
    try:
        (task, pid, cpu,flags, ts, msg) = b.trace_fields()
    except ValueError:
        continue
    print("%-18s %-16s %-6s %s" % (ts, task, pid, msg))


