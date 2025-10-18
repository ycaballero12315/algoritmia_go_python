package algoritmia

func HashMap(name string) int {
	usuarios := map[string]int{
	"yoe": 41,
	"duni": 44,
	"sofi": 10,
	"samu": 8,
    }

	edad := usuarios[name]
	return edad
}
