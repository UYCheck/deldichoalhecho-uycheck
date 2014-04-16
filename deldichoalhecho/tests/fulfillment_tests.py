from django.test import TestCase
from django.utils.timezone import now
from popit.models import ApiInstance, Person as PopitPerson
from popolo.models import Person
from ..models import Promise, InformationSource, Fulfillment

nownow = now()

class FulfillmentTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")
        self.promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                        )
        self.promise.fulfillment.delete()

    def test_instanciate_a_fulfillment(self):
        '''Instanciate a Fulfillment'''
        fulfillment = Fulfillment.objects.create(promise=self.promise,\
                                                 percentage=100)

        self.assertTrue(fulfillment)
        self.assertEquals(fulfillment.promise, self.promise)
        self.assertEquals(fulfillment.percentage, 100)
