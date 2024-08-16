# Install Rust for cryptographic library support
RUN curl --proto '=https' --tlsv1.3 https://sh.rustup.rs -sSf | sh

# Install dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libhdf5-dev \
    libssl-dev \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Jupyter and notebook
RUN pip install jupyterlab notebook

# Set environment variable to disable Rust compilation in the cryptography library
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# Copy application into the container and set the working directory
COPY . /app
WORKDIR /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add a user for Jupyter and set the shell
RUN useradd -ms /bin/bash jupyter
USER jupyter

# Expose the port for Jupyter Notebook
EXPOSE 8888

# Set the entry point to start Jupyter Notebook
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
