package com.zcha.dancinglinks.dlxalgorithm;

class Header implements Linked {

    int linkedListLength;
    int index;
    Linked linkAbove;
    Linked linkBelow;
    Linked linkLeft;
    Linked linkRight;


    /**
     * Create a header
     * @param linkedListLength
     * @param index
     * @param linkAbove
     * @param linkBelow
     * @param linkLeft
     * @param linkRight
     */
    Header(int linkedListLength, int index, Linked linkAbove, Linked linkBelow, Linked linkLeft, Linked linkRight) {
        this.linkedListLength = linkedListLength;
        this.index = index;
        this.linkAbove = linkAbove;
        this.linkBelow = linkBelow;
        this.linkLeft = linkLeft;
        this.linkRight = linkRight;
    }


    /**
     * Sets:
     *    - the left links right link to current Headers left link
     *    - the right links left link to current Headers right link
     */
    void unlinkHorizontally() {
        getLinkLeft().setLinkRight(getLinkRight());
        getLinkRight().setLinkLeft(getLinkLeft());
    }


    /**
     * Sets:
     *    - the left links right link to current Header
     *    - the right links left link to current Header
     */
    void linkHorizontally() {
        getLinkLeft().setLinkRight(this);
        getLinkRight().setLinkLeft(this);
    }


    /**
     * @return the length of the linked list
     */
    public int getLinkedListLength() {
        return linkedListLength;
    }


    /**
     * Sets the length of the linked list
     * @param linkedListLength
     */
    public void setLinkedListLength(int linkedListLength) {
        this.linkedListLength = linkedListLength;
    }


    /**
     * @return the current Header index
     */
    public int getIndex() {
        return index;
    }


    /**
     * Sets the current Header index
     * @param index
     */
    public void setIndex(int index) {
        this.index = index;
    }



    @Override
    public void setLinkBelow(Linked nextLinkBelow) {
        this.linkBelow = nextLinkBelow;
    }


    @Override
    public Linked getLinkBelow() {
        return linkBelow;
    }


    @Override
    public void setLinkAbove(Linked nextLinkAbove) {
        this.linkAbove = nextLinkAbove;
    }


    @Override
    public Linked getLinkAbove() {
        return linkAbove;
    }


    @Override
    public void setLinkLeft(Linked linkLeft) {
        this.linkLeft = linkLeft;
    }


    @Override
    public Linked getLinkLeft() {
        return linkLeft;
    }


    @Override
    public void setLinkRight(Linked linkRight) {
        this.linkRight = linkRight;
    }


    @Override
    public Linked getLinkRight() {
        return linkRight;
    }
}
