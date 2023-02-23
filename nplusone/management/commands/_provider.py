import factory
from faker import Factory

from nplusone.models import Tag, UploadDay, Writer, WebToon

fake_ko = Factory.create('ko_KR')


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.sequence(lambda _: fake_ko.word())


class UploadDayFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UploadDay

    day = factory.sequence(lambda _: fake_ko.day_of_week())


class WriterFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Writer

    name = factory.sequence(lambda _: fake_ko.name())


class WebToonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WebToon

    title = factory.sequence(lambda _: fake_ko.text(max_nb_chars=12))
    summary = factory.sequence(lambda _: fake_ko.text(max_nb_chars=50))
    writer = factory.SubFactory(WriterFactory)
    upload_date = factory.SubFactory(UploadDayFactory)
    tag = factory.RelatedFactory(TagFactory)
