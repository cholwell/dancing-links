package com.zcha.dancinglinks.dlxalgorithm;

class Node implements Linked {

    int parentOption;
    int parentHeader;
    int index;
    Linked linkAbove;
    Linked linkBelow;


    /**
     * Create a Node
     * @param parentOption
     * @param parentHeader
     * @param index
     * @param linkAbove
     * @param linkBelow
     */
    Node(int parentOption, int parentHeader, int index, Node linkAbove, Node linkBelow) {
        this.parentOption = parentOption;
        this.parentHeader = parentHeader;
        this.index = index;
        this.linkAbove = linkAbove;
        this.linkBelow = linkBelow;
    }


    /**
     * Sets:
     *    - the above links below link to current Nodes below link
     *    - the below links above link to current Nodes above link
     */
    void unlinkVertically() {
        getLinkAbove().setLinkBelow(getLinkBelow());
        getLinkBelow().setLinkAbove(getLinkAbove());
    }


    /**
     * Sets:
     *    - the above links below link to current Node
     *    - the below links above link to current Node
     */
    void linkVertically() {
        getLinkAbove().setLinkBelow(this);
        getLinkBelow().setLinkAbove(this);
    }


    /**
     * @return the parent option index
     */
    int getParentOption() {
        return parentOption;
    }


    /**
     * Sets the parent option index
     * @param parentOption
     */
    void setParentOption(int parentOption) {
        this.parentOption = parentOption;
    }


    /**
     * @return the parent header index
     */
    int getParentHeader() {
        return parentHeader;
    }


    /**
     * Sets the parent header index
     * @param parentHeader
     */
    void setParentHeader(int parentHeader) {
        this.parentHeader = parentHeader;
    }


    /**
     * @return the current Node index
     */
    int getIndex() {
        return index;
    }


    /**
     * Sets the current Node index
     * @param index
     */
    void setIndex(int index) {
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
        //No op
    }


    @Override
    public Linked getLinkLeft() {
        return null;
    }


    @Override
    public void setLinkRight(Linked linkRight) {
        //No op
    }


    @Override
    public Linked getLinkRight() {
        return null;
    }
}
