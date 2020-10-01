package com.zcha.dancinglinks.dlxalgorithm;

interface Linked {

     /**
      * Sets the link below
      * @param nextLinkBelow
      */
     void setLinkBelow(Linked nextLinkBelow);

     /**
      * @return the link below
      */
     Linked getLinkBelow();

     /**
      * Sets the link above
      * @param nextLinkAbove
      */
     void setLinkAbove(Linked nextLinkAbove);

     /**
      * @return the link above
      */
     Linked getLinkAbove();

     /**
      * Sets the link left
      * @param linkLeft
      */
     void setLinkLeft(Linked linkLeft);

     /**
      * @return the link left
      */
     Linked getLinkLeft();

     /**
      * Set the link right
      * @param linkRight
      */
     void setLinkRight(Linked linkRight);

     /**
      * @return the link right
      */
     Linked getLinkRight();
}
