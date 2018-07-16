from mnist import MNIST

def main():
	mndata = MNIST('MNIST-data')
	mndata.gz = True

	train_images, train_labels = mndata.load_training()
	test_images, test_labels = mndata.load_testing()

	return(train_images, train_labels, test_images, test_labels)

if __name__ == "__main__":
	main()