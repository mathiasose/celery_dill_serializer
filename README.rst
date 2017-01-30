celery_dill_serializer
======================

NameError when running serialized functions
-------------------------------------------

There are some issues with ``NameError``s when serialized functions depend on values defined outside of the scope of the `def`.
Try putting imports and such inside the function definition, i.e.

.. code-block:: python
    
    def make_me_a_pi():
        import math
        return math.pi

as opposed to 

.. code-block:: python
    
    import math
    
    def make_me_a_pi():
        return math.pi
        
which would result in ``NameError: name 'math' is not defined``
