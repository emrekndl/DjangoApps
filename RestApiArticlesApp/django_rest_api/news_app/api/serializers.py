from rest_framework import serializers
from news_app.models import Article, Author

from datetime import datetime, date
from django.utils.timesince import timesince


class ArticleSerializer(serializers.ModelSerializer):
    """ Serializer for articles """
    time_since_pub = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField(read_only=True)
    # author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = 'create_date', 'update_date'
        read_only_fields = 'id', 'create_date', 'update_date'

    def get_time_since_pub(self, obj):
        """ Get time since pub date """
        if obj.active:
            now = datetime.now()
            pub_date = obj.pub_date
            return f'{timesince(pub_date, now)} ago'
        return 'Article is not active'

    def validate_pub_date(self, value):
        """ Validate pub date """
        if value > date.today():
            raise serializers.ValidationError('Pub date must be in the past')
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """ Author serializer """
    # author_articles = ArticleSerializer(many=True, read_only=True)
    author_articles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='article-detail'
        )

    class Meta:
        model = Author
        fields = '__all__'


""" Default serializer """

# class ArticleSerializer(serializers.Serializer):
#     """ Serializer for Article model """

#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     text = serializers.CharField()
#     city = serializers.CharField()
#     pub_date = serializers.DateField()
#     active = serializers.BooleanField()
#     create_date = serializers.DateTimeField(read_only=True)
#     update_date = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.text = validated_data.get('text', instance.text)
#         instance.city = validated_data.get('city', instance.city)
#         instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):  # object validation
#         if data['title'] == data['description']:
#             raise serializers.ValidationError("Title and description must be different")
#         return data

#     def validate_title(self, value):  # field validation
#         if len(value) < 10:
#             raise serializers.ValidationError(f"Title must be at least 10 characters long, you entered {len(value)} characters")
#         return value
