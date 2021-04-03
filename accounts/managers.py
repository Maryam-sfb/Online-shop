from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, password, address, phone_number):
        if not email:
            raise ValueError('Users must have an email!')
        if not full_name:
            raise ValueError('Users must have a full name!')

        user = self.model(email=self.normalize_email(email), full_name=full_name, address=address, phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password, address, phone_number):
        user = self.create_user(email=self.normalize_email(email), full_name=full_name, password=password, address=address, phone_number=phone_number)
        user.is_admin = True
        user.save(using=self._db)
        return user