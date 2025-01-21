def howManyPanelsCore(panelHeight :int, panelWidth :int, roofHeight :int, roofWidth :int):
    # Early returns
    if panelHeight > roofHeight or panelWidth > roofWidth:
        return 0
    # If panels fit perfectly into the roof dimensions, return the product of the number of panels along each dimension
    if roofHeight % panelHeight == 0 and roofWidth % panelWidth == 0:
        return (roofHeight // panelHeight) * (roofWidth // panelWidth)
    else:
        # Check in sort of a raster-Y way, the number of panels that can fit
        # First round will use the panels in a "vertical" orientation
        panelsX = roofWidth // panelWidth
        panelsY = roofHeight // panelHeight

        totalPanels = panelsX * panelsY

        # Check if an extra flipped panel can be fit in the remaining width 
        remainingWidth = roofWidth % panelWidth
        if remainingWidth >= panelHeight:
            newColX = remainingWidth // panelHeight
            newColY = roofHeight // panelWidth
            totalPanels += newColX * newColY

        # Check if a new row can be fit in the remaining height
        remainingHeight = roofHeight % panelHeight
        if remainingHeight >= panelWidth:
            newRowX = roofWidth // panelHeight
            newRowY = remainingHeight // panelWidth
            totalPanels += newRowX * newRowY


        return totalPanels

def howManyPanels(panelHeight :int, panelWidth :int, roofHeight :int, roofWidth :int):
    # Return the maximum number of panels that can fit in the roof dimensions
    # Will check both ways to get a quick-ish "max" number of panels
    return max(howManyPanelsCore(panelHeight, panelWidth, roofHeight, roofWidth), 
               howManyPanelsCore(panelWidth, panelHeight, roofHeight, roofWidth))



if __name__ == "__main__":
    print(howManyPanels(1, 2, 2, 4))  # Example usage
    print(howManyPanels(1, 2, 3, 5))  # Example usage
    print(howManyPanels(2, 2, 1, 10))  # Example usage
    print(howManyPanels(3, 2, 5, 7))  # Example usage
    print(howManyPanels(2, 3, 5, 11))  # Example usage
    