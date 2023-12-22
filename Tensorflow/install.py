# >> activate tensorflow
# >> python (activating python shell)
# >> import tensorflow as tf
# >> hello = tf.constant('Hello, Tensorflow!')
# >> sess = tf.Session()
# >> print(sess.run(hello))


python3 -m venv --system-site-packages ./venv
source ./venv/bin/activate  # sh, bash, or zsh

pip install --upgrade pip

pip list  # show packages installed within the virtual environment
deactivate  # don't exit until you're done using TensorFlow

pip install --upgrade tensorflow

https://www.tensorflow.org/install/pip?hl=zh-cn#ubuntu-macos
