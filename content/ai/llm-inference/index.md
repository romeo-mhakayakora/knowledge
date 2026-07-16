---
title: LLM Inference
---

# LLM Inference

A comprehensive study of large language model serving, from transformer mechanics and hardware execution to optimization algorithms and distributed orchestration.

## Syllabus Roadmap

| Module | Topic | Description | Status |
| :--- | :--- | :--- | :--- |
| **01** | **[Transformer Fundamentals](01-transformer-fundamentals.md)** | Attention mechanisms, encoder vs. decoder, tokenization, embeddings, positional encoding, and KV cache basics. | Not started |
| **02** | **[Autoregressive Decoding](02-autoregressive-decoding.md)** | Prefill vs. decode phases, causal attention, greedy/beam search, top-k/top-p sampling, temperature, and speculative decoding. | Not started |
| **03** | **[GPU & CUDA Basics](03-gpu-cuda-basics.md)** | GPU architecture, CUDA kernels, memory hierarchy (HBM, SRAM, registers), kernel launches, tensor cores, and memory bandwidth. | Not started |
| **04** | **[PyTorch Execution](04-pytorch-execution.md)** | Eager mode, torch.compile, custom operators, dynamic shapes, and memory management inside PyTorch. | Not started |
| **05** | **[Model Compression](05-model-compression.md)** | FP16/BF16 representation, INT8/INT4 quantization, weight-only/activation quantization, GPTQ, AWQ, GGUF, and KV cache quantization. | Not started |
| **06** | **[Serving Architecture](06-serving-architecture.md)** | API servers, OpenAI-compatible endpoints, FastAPI request lifecycle, batching systems, and streaming responses. | Not started |
| **07** | **[LLM Inference Engines](07-llm-inference-engines.md)** | Comparative study of engines: vLLM, TensorRT-LLM, SGLang, Hugging Face TGI, LMDeploy, llama.cpp, Ollama, and ONNX Runtime GenAI. | Not started |
| **08** | **[Scheduling](08-scheduling.md)** | Continuous/iteration-level batching, request queues, paged attention, memory fragmentation, and KV cache allocation. | Not started |
| **09** | **[KV Cache Optimization](09-kv-cache-optimization.md)** | Prefix caching, LMCache, cache reuse across requests, CPU/SSD offloading, disaggregated prefill, and cache eviction strategies. | Not started |
| **10** | **[Performance Metrics](10-performance-metrics.md)** | Time-to-First-Token (TTFT), Time-Per-Output-Token (TPOT), throughput vs. latency tradeoffs, GPU/memory utilization, concurrency, and tail latency. | Not started |
| **11** | **[Distributed Inference](11-distributed-inference.md)** | Tensor parallelism (TP), pipeline parallelism (PP), multi-GPU/multi-node scaling, and communication collectives (All-Reduce, All-Gather). | Not started |
| **12** | **[Production Deployment](12-production-deployment.md)** | Autoscaling policies, load balancing strategies, observability (Prometheus/Grafana metrics), request tracing, fault tolerance, and cost optimization. | Not started |
