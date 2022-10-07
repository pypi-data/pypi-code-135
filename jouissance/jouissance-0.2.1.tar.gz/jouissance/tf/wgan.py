""" jouissance.tf.wgan """

import tensorflow as tf


# pylint: disable-all
# flake8: noqa
class UNetWGAN(tf.keras.Model):  # pylint: disable=too-many-instance-attributes
    """ WGAN-GP.
        Based on: https://keras.io/examples/generative/wgan_gp/
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        discriminator,
        generator,
        d_optimizer, g_optimizer, d_loss_fn, g_loss_fn,
        discriminator_extra_steps=3,
        generator_extra_steps=1,
        gp_weight=10.0,
    ):
        """ Initialize the model.
        """
        super().__init__()
        self.discriminator = discriminator
        self.generator = generator
        self.d_steps = discriminator_extra_steps
        self.g_steps = generator_extra_steps
        self.gp_weight = gp_weight
        self.d_optimizer = d_optimizer
        self.g_optimizer = g_optimizer
        self.d_loss_fn = d_loss_fn
        self.g_loss_fn = g_loss_fn

    def gradient_penalty(
        self, batch_size, real_images, fake_images, conditions
    ):
        """ Calculates the gradient penalty.

        This loss is calculated on an interpolated image
        and added to the discriminator loss.
        """
        # Get the interpolated image
        alpha = tf.random.normal([batch_size, 1, 1, 1], 0.0, 1.0)
        diff = fake_images - real_images
        interpolated = real_images + alpha * diff

        with tf.GradientTape() as gp_tape:
            gp_tape.watch(interpolated)
            # 1. Get the discriminator output for this interpolated image.
            pred = self.discriminator(
                [conditions, interpolated], training=True)

        # 2. Calculate the gradients w.r.t to this interpolated image.
        grads = gp_tape.gradient(pred, [interpolated])[0]
        # 3. Calculate the norm of the gradients.
        norm = tf.sqrt(tf.reduce_sum(tf.square(grads), axis=[1, 2, 3]))
        return tf.reduce_mean((norm - 1.0) ** 2)

    def train_step(self, data_batch):  # pylint: disable=too-many-locals
        """ override train step """
        real_images, conditions = data_batch
        if isinstance(real_images, tuple):
            real_images = real_images[0]

        # Get the batch size
        batch_size = tf.shape(real_images)[0]
        # For each batch, we are going to perform the
        # following steps as laid out in the original paper:
        # 1. Train the generator and get the generator loss
        # 2. Train the discriminator and get the discriminator loss
        # 3. Calculate the gradient penalty
        # 4. Multiply this gradient penalty with a constant weight factor
        # 5. Add the gradient penalty to the discriminator loss
        # 6. Return the generator and discriminator losses as a loss dictionary

        # Train the discriminator first. The original paper recommends training
        # the discriminator for `x` more steps (typically 5) as compared to
        # one step of the generator. Here we will train it for 3 extra steps
        # as compared to 5 to reduce the training time.
        random_latent_vectors = tf.random.normal(tf.shape(conditions))
        for _ in range(self.d_steps):
            # Get the latent vector
            with tf.GradientTape() as tape:
                # Generate fake images from the latent vector
                fake_images = self.generator(
                    [conditions, random_latent_vectors], training=True)
                # Get the logits for the fake images
                fake_logits = self.discriminator(
                    [conditions, fake_images], training=True)
                # Get the logits for the real images
                real_logits = self.discriminator(
                    [conditions, real_images], training=True)

                # Calculate the discriminator loss using the fake and real image logits
                d_cost = self.d_loss_fn(
                    real_log=real_logits, fake_log=fake_logits,
                    real_img=real_images, fake_img=fake_images)
                try:
                    scaled_d_cost = self.d_optimizer.get_scaled_loss(d_cost)
                except:  # pylint: disable=bare-except
                    scaled_d_cost = d_cost
                # Calculate the gradient penalty
                gdp = self.gradient_penalty(
                    batch_size, real_images, fake_images, conditions)
                # Add the gradient penalty to the original discriminator loss
                scaled_d_loss = scaled_d_cost + gdp * self.gp_weight
                d_loss = d_cost + gdp * self.gp_weight

            # Get the gradients w.r.t the discriminator loss
            scaled_d_gradient = tape.gradient(
                scaled_d_loss, self.discriminator.trainable_variables)
            try:
                d_gradient = self.d_optimizer.get_unscaled_gradients(
                    scaled_d_gradient)
            except:  # pylint: disable=bare-except
                d_gradient = scaled_d_gradient

            # Update the weights of the discriminator using the discriminator optimizer
            self.d_optimizer.apply_gradients(
                zip(d_gradient, self.discriminator.trainable_variables)
            )

        # Train the generator
        # Get the latent vector
        for _ in range(self.g_steps):
            with tf.GradientTape() as tape:
                # Generate fake images using the generator
                generated_images = self.generator(
                    [conditions, random_latent_vectors], training=True)
                # Get the discriminator logits for fake images
                gen_img_logits = self.discriminator(
                    [conditions, generated_images], training=True)
                # Calculate the generator loss
                g_loss = self.g_loss_fn(
                    fake_log=gen_img_logits, fake_img=generated_images, real_img=real_images)
                try:
                    scaled_g_loss = self.g_optimizer.get_scaled_loss(g_loss)
                except:  # pylint: disable=bare-except
                    scaled_g_loss = g_loss
            # Get the gradients w.r.t the generator loss
            scaled_gen_gradient = tape.gradient(
                scaled_g_loss, self.generator.trainable_variables)
            try:
                gen_gradient = self.g_optimizer.get_unscaled_gradients(
                    scaled_gen_gradient)
            except:  # pylint: disable=bare-except
                gen_gradient = scaled_gen_gradient
            # Update the weights of the generator using the generator optimizer
            self.g_optimizer.apply_gradients(
                zip(gen_gradient, self.generator.trainable_variables)
            )
        return {"d_loss": d_loss, "g_loss": g_loss}
