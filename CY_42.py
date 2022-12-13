'''# Example 4: using size attribute, we can see data points having different size.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", 
            y="tip",
            hue="day",
            size="size",
            data=tips)
plt.show()


# Example 1: Using relplot() to visualize tips dataset
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x ="total_bill", y ="tip", data = tips)
plt.show()

# Example 2: Using relplot() with kind=”scatter”.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x ="total_bill",
            y ="tip",
            kind ="scatter",
            data = tips)
plt.show()

# Example 3: Using relplot() with kind=”line”.
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style ="ticks")
tips = sns.load_dataset('tips')
sns.relplot(x ="total_bill",
            y ="tip",
            kind ="line",
            data = tips)
plt.show()'''

# Though both these plots can be drawn using relplot(),
# seaborn also have separate functions for visualizing these kind of plots. 
# These functions do provides some other functionalities too, compared to relplot().