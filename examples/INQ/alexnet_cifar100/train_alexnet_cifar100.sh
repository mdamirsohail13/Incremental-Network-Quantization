./build/tools/caffe train \
    	--solver=./examples/alexnet_cifar100/solver.prototxt \
	--gpu=2 &> ./examples/alexnet_cifar100/alexnet_cifar100_5-bit-inq-solver-train-out.txt
