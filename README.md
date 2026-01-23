# Homework 1: Docker, SQL and Terraform

**Data Engineering Zoomcamp 2026**  
**Due date:** 27 January 2026

---

## Question 1: What's the version of pip in the python:3.13 image?

**Explanation:** The official `python:3.13` Docker image comes with pip version 25.3 preinstalled.

**Command used to check:**
```bash
docker run -it --rm --entrypoint bash python:3.13 -c "
python --version
pip --version
"
