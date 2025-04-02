�
    ��Rg�  �                   �t  � d dl mZ d dlmZ d dlmZ d dlmZ d dl mZ ddl	m
Z
mZ d dlmZ d d	lmZ d d
lmZ d dlmZ d dlmZ d dlmZ d dlmZ d dlZddlmZ  e�   �         Z G d� de�  �        Z G d� de�  �        Zd� Zd� Zd� Zd� Zd� Z d� Z!d� Z" G d� de�  �        Z#ddlmZ  G d� de�  �        Z$dS )�    )�get_user_model��status)�Response)�APIView)�authenticate�   )�RegisterSerializer�LoginSerializer)�Token��render)�redirect)�HttpResponseRedirect)�	send_mail)�UserN)�PasswordResetOTPc                   �   � e Zd Zd� ZdS )�RegisterViewc                 ��   � t          |j        ��  �        }|�                    �   �         r$|�                    �   �          t	          |d�  �        S t          |j        t          j        ��  �        S )N��data�
index.htmlr   )	r
   r   �is_valid�saver   r   �errorsr   �HTTP_400_BAD_REQUEST)�self�request�
serializers      �jC:\Users\tushar sharma\Desktop\WEBDEV\Dotanalytics\integrated_project\DOTANALYTICS\authentication\views.py�postzRegisterView.post   sa   � �'�W�\�:�:�:�
���� � � 	1��O�O�����'�,�0�0�0��
�)�&�2M�N�N�N�N�    N��__name__�
__module__�__qualname__r"   � r#   r!   r   r      s(   � � � � � �O� O� O� O� Or#   r   c                   �   � e Zd Zd� ZdS )�	LoginViewc           	      �  � t          |j        ��  �        }|�                    �   �         �r|j        d         }|j        d         }	 t          j        �                    |��  �        }n2# t          j        $ r  t          ddit          j
        ��  �        cY S w xY wt          |j        |��  �        }|�ht          j        �                    |�	�  �        \  }}|j        d
|j        � d|j        � d|j        � d|j        � �d�}t          |t          j        ��  �        S t          ddit          j
        ��  �        S t          |j        t          j
        ��  �        S )Nr   �email�password�r,   �errorzInvalid email or passwordr   )�usernamer-   )�userz+http://localhost:5173/login-redirect?token=z&email=z&first_name=z&last_name=)�token�redirect_url)r   r   r   �validated_datar   �objects�get�DoesNotExistr   r   r   r   r,   r   �get_or_create�key�
first_name�	last_name�HTTP_200_OKr   )	r   r   r    r,   r-   r1   r2   �created�response_datas	            r!   r"   zLoginView.post"   s�  � �$�'�,�7�7�7�
���� � � 	l��-�g�6�E�!�0��<�H�l��|�'�'�e�'�4�4�����$� l� l� l���*E� F�v�Oj�k�k�k�k�k�k�l����  ���h�G�G�G�D���!&��!<�!<�$�!<�!G�!G���w� �� !e�e�i�  !e�  !e�`d�`j�  !e�  !e�x|�  yH�  !e�  !e�  UY�  Uc�  !e�  !e�!� !��  ��f�6H�I�I�I�I���*E� F�v�Oj�k�k�k�k� �
�)�&�2M�N�N�N�Ns   � A' �',B�BNr$   r(   r#   r!   r*   r*   !   s(   � � � � � �O� O� O� O� Or#   r*   c                 �"   � t          | d�  �        S )Nr   r   �r   s    r!   �homerA   B   �   � ��'�<�(�(�(r#   c                 �"   � t          | d�  �        S )Nz	saas.htmlr   r@   s    r!   �	saas_viewrD   F   s   � ��'�;�'�'�'r#   c                 �"   � t          | d�  �        S )Nz
cyber.htmlr   r@   s    r!   �
cyber_viewrF   J   rB   r#   c                 �"   � t          | d�  �        S )Nzdocker.htmlr   r@   s    r!   �docker_viewrH   M   �   � ��'�=�)�)�)r#   c                 �"   � t          | d�  �        S )NzAI.htmlr   r@   s    r!   �ArtficialIntelligence_viewrK   P   �   � ��'�9�%�%�%r#   c                 �"   � t          | d�  �        S )Nzpython.htmlr   r@   s    r!   �python_viewrN   S   rI   r#   c                 �"   � t          | d�  �        S )NzML.htmlr   r@   s    r!   �MachineLearning_viewrP   V   rL   r#   c                   �   � e Zd Zd� ZdS )�RequestOTPViewc                 �  � |j         �                    d�  �        }	 t          j        �                    |��  �        }t	          j        dd�  �        }||j        _        |j        �                    �   �          t          dd|� d�d|g�  �         t          d	d
it          j        ��  �        S # t          j        $ r  t          ddit          j        ��  �        cY S w xY w)Nr,   r.   i�� i?B zYour OTP for Password ResetzYour OTP is z. It is valid for 10 minutes.zfrom@example.com�messagezOTP sent to your email.r   r/   �$User with this email does not exist.)r   r6   r   r5   �random�randint�profile�otpr   r   r   r   r<   r7   �HTTP_404_NOT_FOUND)r   r   r,   r1   rY   s        r!   r"   zRequestOTPView.post]   s�   � ��� � ��)�)��	q��<�#�#�%�#�0�0�D��.���0�0�C�"�D�L���L�������-�A�s�A�A�A�"���	� � � �Y�(A�B�6�K]�^�^�^�^��� � 	q� 	q� 	q��W�&L�M�V\�Vo�p�p�p�p�p�p�	q���s   �BB* �*,C�CNr$   r(   r#   r!   rR   rR   \   s(   � � � � � �q� q� q� q� qr#   rR   c                   �   � e Zd Zd� ZdS )�ValidateOTPAndResetPasswordViewc                 �  � |j         �                    d�  �        }|j         �                    d�  �        }|j         �                    d�  �        }|j         �                    d�  �        }||k    rt          ddit          j        ��  �        S 	 t
          j        �                    ||��  �        �                    �   �         }|ru|�	                    �   �         ra|j
        }|�                    |�  �         |�                    �   �          |�                    �   �          t          d	d
it          j        ��  �        S t          ddit          j        ��  �        S # t          j        $ r  t          ddit          j        ��  �        cY S w xY w)Nr,   rY   �new_password�confirm_passwordr/   zPasswords do not match.r   )�user__emailrY   rT   zPassword reset successfully.zInvalid or expired OTP.rU   )r   r6   r   r   r   r   r5   �filter�last�is_otp_validr1   �set_passwordr   �deleter<   r   r7   rZ   )r   r   r,   rY   r^   r_   �
otp_recordr1   s           r!   r"   z$ValidateOTPAndResetPasswordView.posts   s�  � ��� � ��)�)���l���u�%�%���|�'�'��7�7��"�<�+�+�,>�?�?���+�+�+��W�&?�@��Id�e�e�e�e�	q�)�1�8�8�U�PS�8�T�T�Y�Y�[�[�J�� j�j�5�5�7�7� j�!����!�!�,�/�/�/��	�	�����!�!�#�#�#���,J� K�TZ�Tf�g�g�g�g���*C� D�V�Mh�i�i�i�i��� � 	q� 	q� 	q��W�&L�M�V\�Vo�p�p�p�p�p�p�	q���s   �B)E �7E �,F�FNr$   r(   r#   r!   r\   r\   r   s(   � � � � � �q� q� q� q� qr#   r\   )%�django.contrib.authr   �rest_frameworkr   �rest_framework.responser   �rest_framework.viewsr   r   �	serilizerr
   r   �rest_framework.authtoken.modelsr   �django.shortcutsr   r   �django.httpr   �django.core.mailr   �django.contrib.auth.modelsr   rV   �modelsr   r   r*   rA   rD   rF   rH   rK   rN   rP   rR   r\   r(   r#   r!   �<module>rr      sq  �� .� .� .� .� .� .� !� !� !� !� !� !� ,� ,� ,� ,� ,� ,� (� (� (� (� (� (� ,� ,� ,� ,� ,� ,� :� :� :� :� :� :� :� :� 1� 1� 1� 1� 1� 1� #� #� #� #� #� #� %� %� %� %� %� %� ,� ,� ,� ,� ,� ,� (� (� (� (� (� (� &� &� &� &� &� &� +� +� +� +� +� +� ���� $� $� $� $� $� $� �~����O� O� O� O� O�7� O� O� O�O� O� O� O� O�� O� O� O�B)� )� )�(� (� (�)� )� )�*� *� *�&� &� &�*� *� *�&� &� &�q� q� q� q� q�W� q� q� q�( %� $� $� $� $� $�q� q� q� q� q�g� q� q� q� q� qr#   