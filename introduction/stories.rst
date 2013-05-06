Requirements Modelling
======================

.. graphviz::

   digraph d {
      node [shape=rectangle];
      edge [arrowhead=crow];

      uc [label="use-case"];
      uc -> mission -> scenario;
      payload -> scenario;
      airframe -> scenario;
   }

The goal of our requirement analysis is to evaluate combinations of hardware that are potentially effective in different mission profiles, and use that information to guide our development program.

Broadly speaking, we have modeled the functional requirements of the Unmanned Aerial System (UAS) as "use cases". These can be thought of as "types of situation where a UAV might be useful".

Use-cases are generic and abstract. We make them more real by describing one or more "mission profile", which are instances (examples of) the use case. Each use case might have a number of mission profiles, representing of the variation in the use case that might be encountered in real life. They are an intermediate level of abstraction, and include details such as a maps, mission brief (SMEAC or equivelent), etc. Mission profiles are the layer where we hoipe to engage discussion with the SAR community.

The finest grain of requirement are "scenarios". These represent a combination of airframe and payload, applied to a mission profile. Scenarios are fine-grained, and contain enough information for us to simulate the performance of some specific hardware against a mission profile. When simulation shows a combination of payload and airframe might be apprpriate for a certain mission profile, the simulartion results will be are presented and discussed.

.. toctree::
   :glob:

   stories/*

use-case ideas
--------------

 * Training - we must be able to provide training to operators
 * System evaluation - users must be able to evaluate tools before they can plan to incorporate them
 * Component evaluation - developers should be able to work with [potential] users to evaluate performance of components (e.g. evaluate thermal camera with SES assistance)

todo: new sections
------------------
 * hardware - airframes
 * hardware - payloads

Only then can we start developing simulations, assessing specific scenarios, etc.
